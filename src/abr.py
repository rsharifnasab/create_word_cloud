#!/usr/bin/python3

##############################
#          IMPORTS
##############################
from wordcloud_fa import WordCloudFa
############################
# the library for creating wordcloud
###########################


from config import *
##################################
# load 3 config dictionaries in config.py
################################

from src.utils import *
################
# load util functions in src/utils.py for loading and cleaning and etc
################


def main():
    """
        main function of the program
        this will do whole thigs you expect from program :D
    """

    context = determine_context()
    # find out where is the  context, is it twitter or telegram or normal text
    # this is the only function that interacts with user directly

    mask = load_mask()
    # load  image file (png or jpg)
    # and process it if its necessary
    # and finally return a numpy array

    stop_words = load_stop_words()
    # load stop words from stop words list

    text, user_id = get_text(context)
    # load text adn find twiter username (to know the address of save file)

    text = clean_text(text = text , context = context, stop_words = stop_words)
    # clean text and remove stop words if it is necessary

    print_stats(text)
    #print some stats to know the program is working well

    wc_instance = WordCloudFa(
        background_color=general_config["BG_COLOR"],
        font_path=general_config["FONT"],
        mask = mask,
        persian_normalize=True,
        include_numbers=False,
        stopwords=stop_words,
    )

    word_cloud = wc_instance.generate(text)
    # genrate the word cloud!

    result_image = word_cloud.to_image()

    OUT_FOLDER = general_config['OUT_FOLDER']

    make_dir(OUT_FOLDER)
    print("saving output image to" + f"{OUT_FOLDER}{user_id}.png")

    result_image.save(f"{OUT_FOLDER}{user_id}.png")
    with open(f"{OUT_FOLDER}cleaned_{user_id}.txt","w") as cleaned_result_file:
        cleaned_result_file.write(text)

    result_image.show()

#####################################################

if __name__=="__main__":
    main()
