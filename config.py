#!/usr/bin/python3

general_config = {
    "MASK" : "./assets/masks/tw",

    "FONT" : "./assets/fonts/shabnam/Shabnam.ttf",

    "OUT_FOLDER" : "./out/",

    "BG_COLOR" : "white",

    "NORMALIZE_MASK" : True,

    "STOP_WORDS_LIST" : [
        "./assets/stop_words/stopwords_me.txt",
        "./assets/stop_words/origianl_stop_words.txt",
        "./assets/stop_words/addtional_stops.txt",
        ],
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
    "SOURCE" :  "./input.txt", #"clipboard" 

}
