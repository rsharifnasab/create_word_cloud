#!/usr/bin/python3

##############################
#          IMPORTS
##############################
from bs4 import BeautifulSoup
from os import system as shell
from glob import glob as glob_path
from wordcloud_fa import WordCloudFa
from numpy import array as np_array
from PIL import Image

######################################
#             CONFIGS
######################################
MASK = "../assets/masks/telegram.png"
FONT = "../assets/fonts/IR/IRNazanin_YasDL.com.ttf"

DEFAULT_INPUT_PATH = './chat-datas/*/*.html'
RESULT_FILE_ADD = "./result.png"

BG_COLOR = "white"


STOP_WRODS_LIST =[
    "../assets/stop_words/stopwords_me.txt",
    "../assets/stop_words/origianl_stop_words.txt",
    "../assets/stop_words/addtional_stops.txt",
]

#########################################
#              the CODE
#########################################
def get_input_folder():
    """
    communicate with user and get address of srouce
    """
    print("please enter path of exported folder")
    print(f"(nothing for default: {DEFAULT_INPUT_PATH})")
    custom_path = input().strip()
    final_path = custom_path+"/*.html" if custom_path !="" else DEFAULT_INPUT_PATH
    return final_path


def load_stop_words():
    """
    load stop words and return them as a set
    it load from 3 files that wrote in STOP_WORDS_LIST
    """
    words = []
    for file_add in STOP_WRODS_LIST:
        with open(file_add,"r") as file:
            new_words = file.read().split()
            words+= new_words
    return set(words)

def clean_word(d):
    """
        remove some bad words from input
        for example twitter links
        or remove nim fasele
        or ...
    """
    d.replace("\u200c","")
    if len(d) <3: return ""
    if "@" in d : return ""
    if "joinchat" in d : return ""

    return d


def print_stats(text):
    """
    show some statistics
    to make sure that the program opened correct input file
    """
    print( f" len e kol : {len(text)}")
    print (f"""spaces count : { text.count(" ") }""" )


list_of_files = glob_path( get_input_folder() )

print("loading files")
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

text = ""
for meta in meta_list:
    if "text" in meta.attrs['class']:
        text += meta.get_text() + " "

print("cleaning")
text = " ".join( [ clean_word(word) for word in text.split() ] )

#################################

print_stats(text)

print("generating cloud")
mask_array = np_array( Image.open(MASK) )

wc_instance = WordCloudFa(
    width=900, height=900,
    background_color=BG_COLOR,
    font_path=FONT,
    mask = mask_array,
    persian_normalize=True,
    include_numbers=False,
    stopwords=load_stop_words(),
)

word_cloud = wc_instance.generate(text)

result_image = word_cloud.to_image()
result_image.save(RESULT_FILE_ADD)
result_image.show()
