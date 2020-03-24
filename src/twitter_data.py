#!/usr/bin/python3

from config import data_config
from json import loads as load_json

def get_text(source : str) -> (str,str):
    """
    load text from input js file
    """
    print(f"loading twitter data file from {source}")
    raw_text_json = open(source, 'r').read()
    
    #ok_first_line junks
    to_remove_len = len("window.YTD.tweet.part0 = ")
    raw_text_json = raw_text_json[to_remove_len: ]
    
    data = load_json(raw_text_json)
    print(f"loaded {len(data)} tweets") 
    
    print("cleaning")
    all_text = []
    for whole_json in data:
        tweet = whole_json["tweet"]
        text = clean_tweet(tweet)
        if text!= "" : all_text.append(text)
    print(f"cleaning complete remained {len(all_text)}")

    return "\n".join(all_text), "data"


def clean_tweet(tweet):
    """ 
    clean every tweet json and return a str contains tweet text
    if will remove mentions or urls baseid on config.py
    """

    if data_config['NO_LINK'] and len(tweet["entities"]["urls"]) > 0 : return "" # linkdar ha ro hazf kon
    if data_config['NO_REPLIES'] and len(tweet["entities"]["user_mentions"]) > 0 : return "" # ounaee ke mention hast ro hazf kon
   
    return tweet["full_text"]
