#!/usr/bin/python3

##############################
#          IMPORTS
##############################

############################
# the library for creating wordcloud
###########################
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator

##################################
# load 3 config dictionaries in config.py
################################
from config import *

################
# load util functions in src/utils.py for loading and cleaning and etc
################
from src.utils import *


def main(inp_text = None):
    """
        main function of the program
        this will do whole thigs you expect from program :D
    """

    context = "text" # determine_context()
    # find out where is the  context, is it twitter or telegram or normal text
    # this is the only function that interacts with user directly

    mask = load_mask()
    # load  image file (png or jpg)
    # and process it if its necessary
    # and finally return a numpy array

    stop_words = load_stop_words()
    # load stop words from stop words list

    text, user_id =  inp_text, "text" #get_text(context)
    # load text adn find twiter username (to know the address of save file)

    text = clean_text(text = text , context = context, stop_words = stop_words)
    # clean text and remove stop words if it is necessary

    print_stats(text)
    #print some stats to know the program is working well


    wc = WordCloud(
        mask=mask,
        background_color= general_config["BG_COLOR"],
        font_path = general_config["FONT"],


        include_numbers=False,
        stopwords=stop_words,

        max_words=general_config["MAX_WORDS"],

        contour_width=general_config["LINE_WIDTH"],
        contour_color=general_config["LINE_COLOR"],

        max_font_size=general_config["MAX_FONT"],
        min_font_size=general_config["MIN_FONT"],

        relative_scaling=0.2,
    )
    wc.generate(text)

    #########
    # generate main image
    #########
    result_image = wc.to_image()

    ##############
    # recolor image based on mask
    # if config[colorful] is true
    #############
    if general_config["COLORFUL_IMAGE"]:
        image_colors = ImageColorGenerator(mask)
        result_image = wc.recolor(color_func=image_colors).to_image()

    #################
    # save result image
    # and cleaned text to out folder
    ################
    # name of text file and image file are based on twitter username
    # in case of telegram or normal text, it it telegram.png or text.png
    ##################
    OUT_FOLDER = general_config['OUT_FOLDER']

    make_dir(OUT_FOLDER)
    print("saving output image to" + f"{OUT_FOLDER}{user_id}.png")

    result_image.save(f"{OUT_FOLDER}{user_id}.png")
    with open(f"{OUT_FOLDER}cleaned_{user_id}.txt","w") as cleaned_result_file:
        cleaned_result_file.write(text)

#    result_image.show()


#####################################################

if __name__=="__main__":
    main()
