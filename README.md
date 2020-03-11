# create word cloud for telgram chat and twitter


## how to use (general)
1. open config.py and set your setting such as input address
2. run program.py with python3.4 or higher
3. select your context (twitter or telegram or normal text)
4. wait until program finishes



## how to use (tweets)
1. you should get tweets from [this site](https://www.allmytweets.net/) and paste to a file for example input.txt
2. enter file address to config.py, twitter_config dictionary
3. if you set 'SOURCE' : "clipboard" program will use system clipboard instead of input file
4. you can set other options in that config
 + no_retweet and no_replis are work as they expected so
 + no link will remove all tweets contains link for example quotes, images and unfollow checker auto tweets


## how to use (telegram)
1. export chat history to a folder
2. enter folder adress in config.py in telegram_config dictionary, something like './input/*.html'



### notes
+ you can set font and mask in general_config file
  + ener a ttf font
  + mask image should be png or jpg
  + you dont need to specify file format! program will guess it

+ if you use third party mask and its not black and white (greyscale for example) you can set NORMALIZE_MASK to True
  + normalize mask is slow operation, it handles greyscale masks, if you use built-in masks you dont need it

+ if stop words didnt removed automatically, set STOP_WORD_CLEAN to "manual" in config.py
+ only if persian words are reversed, make ARABIC_RESHAPER to True


## Requirements
+ wordcloud-fa
+ numpy and PIL (installed by wordcloud-fa)
+ beautifulsoup4 (for parse telegram htmls)
+ arabic reshaper
+ bidi

You can also  install requirements using `requirements.txt` and `pip`:

    pip3 install -r requirements.txt

## todo
+ write documentation
+ add commandline argument parse
+ add twint support in abr.py

## special thank from:

+ [Mohammadreza Alihoseiny](https://github.com/alihoseiny/) for developing wordcloud-fa and writing [this blog post](https://blog.alihoseiny.ir/%DA%86%DA%AF%D9%88%D9%86%D9%87-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D8%A7%D8%A8%D8%B1-%DA%A9%D9%84%D9%85%D8%A7%D8%AA-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%A8%D8%B3%D8%A7%D8%B2%DB%8C%D9%85%D8%9F/)

+ [amueller](https://github.com/amueller) for developing wordcloud package

+ [Ali Yoonesi](https://github.com/AYoonesi) for good advices and troubleshoots

+ [Radin Shayanfar](https://github.com/radinshayanfar) for pull requests and bug fixes
