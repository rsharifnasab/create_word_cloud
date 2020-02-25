#!/usr/bin/python3

from wordcloud_fa import WordCloudFa
import numpy as np
from PIL import Image


DEFAULT_FILE = "t.txt"
MASK = "assets/masks/tw.png"
FONT = "assets/fonts/font2.ttf"
BG_COLOR = "white"
STOP_WRODS_LIST =[
    "assets/stopwords_me.txt",
    "assets/origianl_stop_words.txt",
    "assets/addtional_stops.txt",
]

def load_stop_words():
    words = []
    for file in STOP_WRODS_LIST:
        new_words = open(file,"r").read().split()
        words+= new_words
    return set(words)

def clean_word(d):
    d.replace("\u200c","")
    if "twitter" in d : return ""
    if ".com" in d : return ""
    if "http" in d : return ""
    if "t.co" in d : return ""
    if len(d) <3: return ""

    return d

def extract_text(line):
    line = line.strip()
    words = line.split(" ")
    while words[0].startswith("@"):
        words = words[1:]

    if words[0] == "RT" : return "" # ignore retwetts
    words = words[:-3]
    words_cleaned = [ clean_word(t) for t in words ]
    return " ".join(words_cleaned)



file_name = input("enter tweets filename: ")
if file_name.strip() == "" : file_name = DEFAULT_FILE

raw_list = open(file_name, "r").read().split("\n")


idish = raw_list[3].replace("@","")
print(f"working on @{idish}\n")


raw_tweets_list = raw_list[10:-6] # start to end!
texts = [ extract_text(t) for t in raw_tweets_list ]

text = " ".join(texts)


print( f" len e kol : {len(text)}")
print (f"""spaces count : { len( text.split(" ") ) }""" )

mask_array = np.array( Image.open(MASK) )

wc = WordCloudFa(
    width=900, height=900,
    background_color=BG_COLOR,
    font_path=FONT,
    mask = mask_array,
    persian_normalize=True,
    include_numbers=False,
    stopwords=load_stop_words(),
)


word_cloud = wc.generate(text)

image = word_cloud.to_image()
image.save(f"out/{idish}.png")
image.show()
