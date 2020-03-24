#!/usr/bin/python3

import twint
from json import loads as jsread

#from wordcloud_fa import WordCloudFa
import numpy as np
from PIL import Image

print("warning: deprecated version, its just for testing twint")

idish =  input("enter username: ")


def fetch_tweet():
    f = open("out/tweets.json","w")
    f.write("")
    f.close()

    c = twint.Config()

    c.Username = idish
    c.Limit = 600
    c.Output = "out"
    c.stats = True
    c.Store_json = True
    c.Filter_retweets = True

    twint.run.Search(c)


fetch_tweet()

print("\n-------fetching tweets done ------\n")


###########################################3
tweet_file = open("out/tweets.json","r").read()
tweet_json_str = tweet_file.split("\n")


def ok(t):
    #if len(t['mentions'])>0 : return False
    if len(t['retweet_date'])>0 : return False
    if len(t['quote_url'])>0 : return False
    if len(t['photos'])>0 : return False


    return True

def clean(d):
    d.replace("\u200c"," ")
    if "twitter" in d : return ""
    if ".com" in d : return ""
    if "http" in d : return ""
    if len(d) <3 : return ""


    #d.replace("")
    return d


tweet_dict = []
for i in range(len(tweet_json_str)-1):
    t = tweet_json_str[i]
    d = jsread(t)

    if not ok(d): continue
    tweet_dict.append(d)


tweets_simple = [ clean(t['tweet']) for t in tweet_dict ]

#print( "\n----\n".join(tweets_simple) )

to_print = "\n\n".join(tweets_simple)

f = open("out/cleaned.txt","w")
f.write(to_print)
f.close()

#######################################

mask_array = np.array(
    Image.open("masks/tw.png")
)

with open('out/cleaned.txt', 'r') as file:
    text = file.read()

    wc = WordCloudFa(
        width=900, height=900,
        background_color="white",
        font_path="fonts/font2.ttf",
        mask = mask_array,
        persian_normalize=True,
        include_numbers=False,
    )

    word_cloud = wc.generate(text)

    image = word_cloud.to_image()
    image.save(f"out/{idish}.png")
    image.show()
