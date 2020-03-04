#!/usr/bin/python3
# coding=utf-8
##############################
#          IMPORTS
##############################
from wordcloud_fa import WordCloudFa
from numpy import array as np_array
from PIL import Image as PIL_Image
from clipboard import paste
from os.path import exists as path_exists
from os import makedirs
import matplotlib.pyplot as plt
import re

######################################
#             CONFIGS
######################################
MASK = "../assets/masks/twitter.png"

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
    #"../assets/stop_words/stopwords_me.txt",
    #"../assets/stop_words/origianl_stop_words.txt",
    "../assets/stop_words/addtional_stops.txt",
]


#########################################
#              the CODE
#########################################

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
    if "t.co" in d : return ""
    if len(d) <3: return ""
    if "-" in d : return ""
    
    if " می" in d  or "شه" in d  : return ""
    if "بیش" in d  : return ""
    if "می" in d : return ""
    if d == "ست" : return ""
    if "خیلی" in d : return ""
    if "ولی" in d : return ""
    
    stp_words = load_stop_words()
    for stp in stp_words:
        if stp in d : return "" 
    return d
    

def extract_text(line):
    """
        get a line of input
        and remove junk file of it
        and clean each word ant etc..
    """
    words = line.strip().split(" ")

    if NO_LINK and "t.co" in line: return "" # linkdar ha ro hazf kon
    words.append("")
    while words[0].startswith("@"): # mention ha ro hazf kon
        if NO_REPLIES : return "" # kolan bikhial in tweet besho
        words = words[1:]

    if NO_RETWEET and words[0] == "RT" : return "" # retwetts ha ro hazf kon

    words = words[:-3] # remove date and time

    words_cleaned = [ clean_word(t) for t in words ]
    return " ".join(words_cleaned)


def get_raw_str():
    """
        get input from input source
        either clipboard or the input file
    """
    file_name = input("enter tweets filename: ")
    print(f"working on @" + file_name, "\n")
    if file_name.strip() == "" :
        print("using clipboard as source")
        return paste()
    else:
        with open(file_name, "r") as input_file:
            return input_file.read()

def print_stats(text):
    """
    show some statistics
    to make sure that the program opened correct input file
    """
    print( f" len e kol : {len(text)}")
    print (f"""spaces count : { text.count(" ") }""" )


def make_dir(dir):
    """
    make the output directory if it isnt there!
    """
    if not path_exists(dir):
        makedirs(dir)
        print(f"Created {dir} directory")

###########################################
def rm_unwanted(text):
    unwanted = re.compile("["
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
                               "]+", flags=re.UNICODE)
    return unwanted.sub(r'', text)
###########################################

raw_str = get_raw_str()
raw_list = raw_str.split("\n")
try:
    user_id = raw_list[3].replace("@","").strip()
except IndexError:
    print("bad input! please copy whole page")
    exit()



raw_tweets_list = raw_list[10:-6] # remove up and down header footer
text_list = [ extract_text(t) for t in raw_tweets_list ]
text = " ".join(text_list)

from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display
text = rm_unwanted(text)
text = get_display(arabic_reshaper.reshape(text))

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
with open(f"{OUT_FOLDER}{user_id}.txt","w") as result_file:
    result_file.write(raw_str)
with open(f"{OUT_FOLDER}cleaned_{user_id}.txt","w") as cleaned_result_file:
    cleaned_result_file.write(text)

result_image.show()

plt.imshow(word_cloud)
plt.axis('off') 
plt.savefig('out/wc.png', dpi=1800)  #instead of result_image.save()
plt.close()
plt.show()
