#!/usr/bin/python3

##############################
#          IMPORTS
##############################
from wordcloud_fa import WordCloudFa


from config import general_config
from config import twitter_config
from config import telegram_config
from utils import *

def main():

    context = determine_context()
    mask = load_mask()
    stop_words = load_stop_words()
    text = get_text(context)
    text = clean_text(text = text , context = context)
    print_stats(text)


    wc_instance = WordCloudFa(
        background_color=general_config["BG_COLOR"],
        font_path=general_config["FONT"],
        mask = mask,
        persian_normalize=True,
        include_numbers=False,
        stopwords=stop_words,
    )

    word_cloud = wc_instance.generate(text)

    result_image = word_cloud.to_image()

    OUT_FOLDER = general_config['OUT_FOLDER']

    make_dir(OUT_FOLDER)
    user_id  = "2"
    result_image.save(f"{OUT_FOLDER}{user_id}.png")
    #with open(f"{OUT_FOLDER}{user_id}.txt","w") as result_file:
    #    result_file.write(raw_str)
    with open(f"{OUT_FOLDER}cleaned_{user_id}.txt","w") as cleaned_result_file:
        cleaned_result_file.write(text)


    result_image.show()

if __name__=="__main__":
    main()
