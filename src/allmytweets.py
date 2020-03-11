#!/usr/bin/python3

from clipboard import paste

from config import twitter_config


def get_text(source : str) -> (str,str):
    raw_str = None

    if source == "clipboard":
        print("using clipboard as source")
        raw_str = paste()
    else:
        print(f"loading allmytweets file from {source}")
        with open(source, "r") as input_file:
            raw_str = input_file.read()

    raw_list = raw_str.split("\n")

    try:
        user_id = raw_list[3].replace("@","").strip()
    except IndexError:
        print("bad enter! please copy whole page")
        exit()

    print(f"working on @{user_id}\n")

    raw_tweet_list = raw_list[10:-6] # remove up and down header footer
    text = [ clean_line(line) for line in raw_tweet_list ]

    return "\n".join(text), user_id



def clean_line(line : str) -> str:
    """
        get a line of input
        and remove junk file of it
        and clean each word ant etc..
    """
    words = line.strip().split(" ")

    if twitter_config['NO_LINK'] and "t.co" in line: return "" # linkdar ha ro hazf kon

    while words[0].startswith("@"): # mention ha ro hazf kon
        if twitter_config['NO_REPLIES'] : return "" # kolan bikhial in tweet besho
        words = words[1:]

    if twitter_config['NO_RETWEET'] and words[0] == "RT" : return "" # retwetts ha ro hazf kon

    words = words[:-3] # remove date and time

    return " ".join(words)
