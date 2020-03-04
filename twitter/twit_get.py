import tweepy
from wordcloud_fa import WordCloudFa
from os import path
from PIL import Image
import numpy as np
from bidi.algorithm import get_display
import arabic_reshaper
import re
import json


with open('config.json', 'r') as f:
    dev = json.load(f)

dev = dev['twitter']

consKey = dev['consKey'] 
consSecret = dev['consSecret'] 
accessKey = dev['accessKey']
accessSecret = dev['accessSecret']

d = path.dirname(__file__)

auth = tweepy.OAuthHandler(consumer_key=consKey, consumer_secret=consSecret)

auth.set_access_token(accessKey, accessSecret)

api = tweepy.API(auth)

numberOfPages = 1
numberOfTweetsPerPage = 200
counter = 0
cloud = ""
txt = ""

username = input("Enter the username: ")
numberOfTweets = int(input("Enter the number of tweets: "))

if numberOfTweets > 200:
    numberOfPages = int(numberOfTweets/200)
else:
    numberOfTweetsPerPage = numberOfTweets


for i in range(numberOfPages):
    tweets = api.user_timeline(screen_name=username, count=numberOfTweetsPerPage, page=i)
    for each in tweets:
        cloud = each.text
        #cloud = re.sub(r'[A-Za-z@_]*', '', cloud)
        counter += 1
        txt = txt + '\n' + each.text
        print(counter, cloud)

with open('data', 'w') as f:
    f.write(txt)
