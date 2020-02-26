#!/usr/bin/python3

from bs4 import BeautifulSoup
from os import system as shell
from glob import glob as glob_path
from wordcloud_fa import WordCloudFa
from numpy import array as np_array
from PIL import Image

DEFAULT_INPUT_PATH = './chat-datas/*/*.html'
RESULT_FILE_ADD = "./result.png"

MASK = "../assets/masks/telegram.png"
FONT = "../assets/fonts/font2.ttf"

BG_COLOR = "white"

STOP_WRODS_LIST =[
    "../assets/stop_words/stopwords_me.txt",
    "../assets/stop_words/origianl_stop_words.txt",
    "../assets/stop_words/addtional_stops.txt",
]


def get_input_folder():
    print("please enter path of exported folder")
    print("(nothing for default)")
    custom_path = input().strip()
    final_path = custom_path if custom_path !="" else DEFAULT_INPUT_PATH
    return final_path


def load_stop_words():
    words = []
    for file in STOP_WRODS_LIST:
        new_words = open(file,"r").read().split()
        words+= new_words
    return set(words)

def clean_word(d):
    d.replace("\u200c","")
    if len(d) <3: return ""

    #if " می" in d  or "شه" in d  : return ""
    #if "بیش" in d  : return ""
    #if "می" in d : return ""
    #if d == "ست" : return ""

    return d


def print_stats(text):
    print( f" len e kol : {len(text)}")
    print (f"""spaces count : { len( text.split(" ") ) }""" )


list_of_files = glob_path( get_input_folder() )
print("loading files")
loaded_xml = "\n".join( [ open(add,"r").read() for add in list_of_files ] )

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
