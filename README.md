# create word cloud for telgram chat and twitter


## how to use
1. open config.py and set your setting
2. run program.py with python3.4 or higher
3. select your context (twitter or telegram or normal text)
4. wait until program finishes

### notes
+ you can set font and mask in general_config file
  + ener a ttf font
  + mask image should be png or jpg
  + you dont need to specify file format! program will guess it

+ if you use third party mask and its not black and white (greyscale for example) you can set NORMALIZE_MASK to True
  + normalize mask is slow operation, it handles greyscale masks, if you use built-in masks you dont need it

+ if stop words didnt removed automatically, set STOP_WORD_CLEAN to "manual" in config.py
+ only if persian words are reversed, make ARABIC_RESHAPER to True


## requirement
+ wordcloud-fa
+ numpy and PIL (installed by wordcloud-fa)
+ beautifulsoup4 (for parse telegram htmls)

## todo
+ write documentation
+ add commandline argument parse
+ add twint support in abr.py



## tweets
1. you should get tweets from [this site](https://www.allmytweets.net/) and paste to a file for example input.txt
2. enter file address to config.py, twitter_config dictionary
3. if you set 'SOURCE' : "clipboard" program will use system clipboard instead of input file
4. you can set other options in that config
 + no_retweet and no_replis are work as they expected so
 + no link will remove all tweets contains link for example quotes, images and unfollow checker auto tweets


## telegram
1. export chat history to a folder
2. enter folder adress in config.py in telegram_config dictionary, something like './input/*.html'
