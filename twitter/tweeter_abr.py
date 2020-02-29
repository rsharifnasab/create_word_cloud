#!/usr/bin/python3

from wordcloud_fa import WordCloudFa
from numpy import array as np_array
from PIL import Image as PIL_Image
from clipboard import paste
from os.path import exists as path_exists
from os import makedirs

MASK = "../assets/masks/tw.png"

FONT = "../assets/fonts/font2.ttf"
FONT = "../assets/fonts/shabnam/Shabnam.ttf"

OUT_FOLDER = "out/"

BG_COLOR = "white"

###############
#if you have unfollow cheker
# or some thing that post automatically tweet with link
# turn on this option to remove all tweets with links (and links and quets)
###########
NO_LINK = False

###############
# to create cloud based on tweets
# and not replies
# set above boolean to True
# use with cautopn
####################
NO_REPLIES = False

#############
#this option is for ignoring retweets
#because in default we want to create cloud only based on user tweets
#not retweets
##############
NO_RETWEET = True

STOP_WRODS_LIST =[
    "../assets/stop_words/stopwords_me.txt",
    "../assets/stop_words/origianl_stop_words.txt",
    "../assets/stop_words/addtional_stops.txt",
]

def load_stop_words():
    words = []
    for file in STOP_WRODS_LIST:
        new_words = open(file,"r").read().split()
        words+= new_words
    return set(words)

def clean_word(d):
    d.replace("\u200c","")
    if "t.co" in d : return ""
    if len(d) <3: return ""

    if " می" in d  or "شه" in d  : return ""
    if "بیش" in d  : return ""
    if "می" in d : return ""
    if d == "ست" : return ""
    if "خیلی" in d : return ""
    if "ولی" in d : return ""


    return d

def extract_text(line):
    words = line.strip().split(" ")

    if NO_LINK and "t.co" in line: return "" # linkdar ha ro hazf kon

    while words[0].startswith("@"): # mention ha ro hazf kon
        if NO_REPLIES : return "" # kolan bikhial in tweet besho
        words = words[1:]

    if NO_RETWEET and words[0] == "RT" : return "" # retwetts ha ro hazf kon

    words = words[:-3] # remove date and time

    words_cleaned = [ clean_word(t) for t in words ]
    return " ".join(words_cleaned)


def get_raw_str():
    file_name = input("enter tweets filename: ")
    if file_name.strip() == "" :
        print("using clipboard as source")
        return paste()
    else:
        return open(file_name, "r").read()

def print_stats(text):
    print( f" len e kol : {len(text)}")
    print (f"""spaces count : { text.count(" ") }""" )


def make_dir(dir):
    if not path_exists(dir):
        makedirs(dir)
        print(f"Created {dir} directory")


raw_str = get_raw_str()
raw_list = raw_str.split("\n")
try:
    user_id = raw_list[3].replace("@","").strip()
except IndexError:
    print("bad input! please copy whole page")
    exit()

print(f"working on @{user_id}\n")

raw_tweets_list = raw_list[10:-6] # remove up and down header
text_list = [ extract_text(t) for t in raw_tweets_list ]
text = " ".join(text_list)

print_stats(text)

mask_array = np_array( PIL_Image.open(MASK) )

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
make_dir(OUT_FOLDER)
result_image.save(f"{OUT_FOLDER}{user_id}.png")
open(f"{OUT_FOLDER}{user_id}.txt","w").write(raw_str)
result_image.show()
