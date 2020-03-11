#!/usr/bin/python3

##############################
#          IMPORTS
##############################
from wordcloud_fa import WordCloudFa


from config import *
from src.utils import *

def main():

    context = determine_context()
    mask = load_mask()
    stop_words = load_stop_words()
    text, user_id = get_text(context)
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
    print("saving output image to" + f"{OUT_FOLDER}{user_id}.png")

    result_image.save(f"{OUT_FOLDER}{user_id}.png")
    with open(f"{OUT_FOLDER}cleaned_{user_id}.txt","w") as cleaned_result_file:
        cleaned_result_file.write(text)


    result_image.show()

if __name__=="__main__":
    main()
