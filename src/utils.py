#!/usr/bin/python3

from os import makedirs
from PIL import Image as PIL_Image
from numpy import array as np_array
from os.path import exists
from bs4 import BeautifulSoup
from glob import glob as glob_path
from re import compile as regex_compile
from re import UNICODE as regex_UNICODE

from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display

from src.allmytweets import get_text as load_twitter_text
from src.twitter_data import get_text as load_tw_data

from config import *



def determine_context() -> str:
    print("which word cloud you want to create?")
    print("1)twitter  2)telegram 3)normal_text 4)data")
    context = input().strip()
    if context in ["", "1", "tw", "twitter"]: return "twitter"
    elif context in ["2", "tg", "telegram"]: return "telegram"
    elif context in ["3", "text", "normal"]: return "text"
    elif context in ["4", "data"]: return "data"
    else:
        print("invalid input, exiting..")
        exit()

def get_text(context : str):
    if context == "twitter":
        return load_twitter_text(twitter_config['SOURCE'])
    elif context == "telegram":
        return load_telegram_text(telegram_config['SOURCE'])
    elif context == "text":
        return load_normal_text(text_config['SOURCE'])
    elif context == "data":
        return load_tw_data(data_config['SOURCE'])

    raise ValueError("shoudnt reach here!")



def load_mask() -> np_array:
    print("loading mask")

    mask_add = general_config["MASK"]
    mask_add = mask_add.replace(".jpg","").replace(".png","")

    jpg_add = mask_add + ".jpg"
    png_add = mask_add + ".png"

    jpg_image = None

    if exists(jpg_add):
        jpg_image = PIL_Image.open(jpg_add)
        print(f"loaded mask {jpg_add}")
    elif exists(png_add):
        png_image = PIL_Image.open(png_add)
        print(f"loaded mask {png_add}")
        jpg_image = png_image.convert('RGB')
    else:
        print("mask not found")
        exit()

    mask_array = np_array(jpg_image)
    NORMALIZE_MASK_NUMBER = general_config["NORMALIZE_MASK_NUMBER"]
    if general_config["NORMALIZE_MASK"]:
        print("normalizing mask")
        for i in range(len(mask_array)):
            for j in range(len(mask_array[i])):
                old_arr = mask_array[i][j]

                if sum(old_arr)> NORMALIZE_MASK_NUMBER:
                    new_arr = [255,255,255]
                else:
                    new_arr = old_arr 

                mask_array[i][j] = new_arr

    return mask_array


def print_stats(text : str):
    """
    show some statistics
    to make sure that the program opened correct input file
    """
    print( f" len e kol : {len(text)}")
    print (f"""spaces count : { text.count(" ") }""" )


def load_stop_words() -> set:
    """
    load stop words and return them as a set
    it load from 3 files that wrote in STOP_WORDS_LIST
    """
    print("loading stop words")

    words = set([])
    for file_add in general_config["STOP_WORDS_LIST"]:
        with open(file_add,"r") as file:
            new_words = file.read().split()
            words.update(new_words)
    return words

def is_stop_word(word,stop_words):
    for stop_word in stop_words:
        if stop_word in word : return True
    return False

def remove_unwanted_chars(text):
    unwanted = regex_compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u'\U00010000-\U0010ffff'
                               u"\u200d"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\u3030"
                               u"\ufe0f"
                               u"\u2069"
                               u"\u2066"
                               u"\u200c"
                               u"\u2068"
                               u"\u2067"
                               "]+", flags=regex_UNICODE)
    return unwanted.sub(r'', text)


def clean_text(text:str,context:str, stop_words) -> str:
    print("cleaning text")

    text = remove_unwanted_chars(text)
    if general_config["ARABIC_RESHAPER"]:
        text = get_display(arabic_reshaper.reshape(text))

    word_list = text.split(" ")
    general_cleaned = [clean_word(word) for word in word_list]

    custom_cleaned = general_cleaned

    if context == "twitter" or context == "data":
        custom_cleaned = [clean_twitter_word(word) for word in general_cleaned]

    elif context == "telegram":
        custom_cleaned = [clean_telegram_word(word) for word in general_cleaned]

    if general_config["STOP_WORD_CLEAN"] == "manual":
        custom_cleaned = [word for word in custom_cleaned if not is_stop_word(word,stop_words)]

    return " ".join(custom_cleaned)


def clean_word(word: str) -> str:
    """
        remove some bad words from input
        remove nim fasele
        and small words
        or ...
    """

    word.replace("\u200c","")
    if len(word) <3: return ""
    if "-" in word : return ""

    return word




def clean_twitter_word(word : str) -> str:
    if "t.co" in word : return ""
    if "@" in word : return ""
    if "RT" in word : return ""

    return word

def clean_telegram_word(word : str) -> str:
    if "@" in word : return ""
    if "joinchat" in word : return ""

    return word

def load_normal_text(source : str):
    print(f"loading normal text from {source}")
    with open(source,"r") as file:
        return file.read(), "text"


def load_telegram_text(source_dir : str) -> str:
    print(f"loading telegram files from {source_dir}")

    list_of_files = glob_path( source_dir )

    xml_list = []
    for file_add in list_of_files:
        with open(file_add,"r") as file:
            xml_list.append(file.read())
    loaded_xml = "\n".join(xml_list)

    if loaded_xml.strip() == "":
        print("nothing loaded, exiting...")
        exit()

    print("parsing")
    soup = BeautifulSoup(loaded_xml, 'html.parser')

    meta_list = soup.find_all("div")

    text = []
    user_id = 'telegram'
    for meta in meta_list:
        if "text bold" in meta.attrs['class']:
            user_id = meta.get_text()
        elif "text" in meta.attrs['class']:
            text.append(meta.get_text() + " ")

    return " ".join(text), user_id


def make_dir(dir : str):
    """
    make the output directory if it isnt there!
    """
    if not exists(dir):
        makedirs(dir)
        print(f"Created {dir} directory")
