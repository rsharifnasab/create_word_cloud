#!/usr/bin/python3

general_config = {

    ########################
    # output folder to save generated cloud
    #######################
	"OUT_FOLDER" : "./out/",

    ##################
    # the mask!
    # check normalize when mask is grey scale to chage it to black and white
    # colorful image is experimental, it is for image that have white background and good colors
    # in most cases it is not useful!
    ##################
    "MASK" : "./assets/masks/tw",
    "NORMALIZE_MASK" : False,
	"NORMALIZE_MASK_NUMBER" : 200,
    "COLORFUL_IMAGE" : False,

    ############
    # color of background text
    ###########
    "BG_COLOR" : "white",

    ##############
    # setting for the font i should use
    # minimum font size os the size of smallest element in shape
    # maximum font size is max font size for most frequent shape in text
    #############
    "FONT" : "./assets/fonts/shabnam/Shabnam.ttf",
	"MIN_FONT" : 5,
	"MAX_FONT" : 1000,

	###################
	# total number of words in shape
	##################
	"MAX_WORDS" : 1000,


	#################
    #settingfor splitter line
    #the line between texts and white space
    #if width is zero, it isn't shown
    ##################
    "LINE_COLOR" : "steelblue",
    "LINE_WIDTH" : 0,


    #################
    # list of file that contains stop words
    #################
    "STOP_WORDS_LIST" : [
        "./assets/stop_words/stopwords_me.txt",
        "./assets/stop_words/origianl_stop_words.txt",
        "./assets/stop_words/addtional_stops.txt",
        ],

    #############
    # should the script look for stopwords manually or let the library clean them
    # set it to "manual" for manual cleaning
    # set anything else to let the library clean it
    ###########
    "STOP_WORD_CLEAN" : "not manual",

    #######################
    # change this boolean only if you have problem whit persian texts
    ######################
    "ARABIC_RESHAPER" : False,
}

telegram_config = {
    "SOURCE" : './input/*.html',
}

text_config = {
    "SOURCE" : './input.txt',
}

twitter_config = {
    ###############
    #if you have unfollow cheker
    # or some thing that post automatically tweet with link
    # turn on this option to remove all tweets with links (and links and quets)
    ###########
    "NO_LINK" : False,

    ###############
    # to create cloud based on tweets
    # and not replies
    # set above boolean to True
    # use with cautopn
    ####################
    "NO_REPLIES" : False,


    #############
    #this option is for ignoring retweets
    #because in default we want to create cloud only based on user tweets
    #not retweets
    ##############
    "NO_RETWEET" : True,

    ##############
    # where should the program look for tweets
    # it can be clipboard
    # or a file path
    #############
    "SOURCE" : "clipboard" #"./input.txt", #

}


################
# setting of loading exported twitter data
# this mode is experimental
# you should download your twitter data first
# before use this part
################
data_config = {
    ###############
    #if you have unfollow cheker
    # or some thing that post automatically tweet with link
    # turn on this option to remove all tweets with links (and links and quets)
    ###########
    "NO_LINK" : False,

    ###############
    # to create cloud based on tweets
    # and not replies
    # set this boolean to True
    # use with cautopn
    ####################
    "NO_REPLIES" : False,

    ##############
    # where should the program look for tweet.js
    # dont open or edit this file
    # the program will do it all
    #############
    "SOURCE" : "input/data/tweet.js"

}
