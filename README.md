# create word cloud for telgram chat and twitter

## how to use (general)

1. read this file carefully

2. open config.py and set your setting such as input address

3. run program.py with python3.4 or higher

4. select your context (twitter or telegram or normal text or twitter exported data)

5. wait until program finishes



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



## how to use (twitter data)

1. this option is for people who wants a cloud for all tweets not last 3000 tweets
2. first of all you should follow this [link](https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive) to export twitter data, it takes some time! be patient
3. after your data is ready, download and unzip it, we need the `tweet.js` file in next step
4. enter path of `tweet.js` in data folder to the config file (in `config.py/data_config`) 
5. open program and select option `4`
6. you can set NO_REPLIES if you want only your tweets not replies
7. there is no NO_RETWEET option because retweets are not included in exported data 
8. press enter and enjoy :D 

 + no link will remove all tweets contains link for example quotes, images and unfollow checker auto tweets



### notes
+ you can set font and mask in general_config file
  + ener a ttf font
  
  + mask image should be png or jpg

  + you dont need to specify file format! program will guess it
  
    
  
+ if you use third party mask and its not black and white (greyscale for example) you can set NORMALIZE_MASK to True
  
+ normalize mask is slow operation, it handles greyscale masks, if you use built-in masks you dont need it
  
    
  
+ if stop words didn't removed automatically, set STOP_WORD_CLEAN to "manual" in config.py

  

+ only if Persian words are reversed, make ARABIC_RESHAPER to True

  

+ line color and line width are for splitter line between text and whitespace, it maybe good for some cases

  

+ max words and min font and max font are 3 numbers, change them with caution, if the min font is too low or max words is high, whole operation will take much time, if the max font is not so big, cloud is ugly






## Requirements
+ wordcloud
+ numpy and PIL 
+ beautifulsoup4 (for parse telegram htmls)
+ arabic reshaper
+ bidi
+ clipboard

You can also install requirements using `requirements.txt` and `pip`:

    pip3 install -r requirements.txt



## to-do

+ [ ] write better documentation
+ [ ] add command-line argument parse
+ [ ] add well twint support for getting tweets automatically

## special thank from:

+ [Mohammadreza Alihoseiny](https://github.com/alihoseiny/) for developing wordcloud-fa and writing [this blog post](https://blog.alihoseiny.ir/%DA%86%DA%AF%D9%88%D9%86%D9%87-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D8%A7%D8%A8%D8%B1-%DA%A9%D9%84%D9%85%D8%A7%D8%AA-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%A8%D8%B3%D8%A7%D8%B2%DB%8C%D9%85%D8%9F/)

+ [amueller](https://github.com/amueller) for developing wordcloud package

+ [Ali Yoonesi](https://github.com/AYoonesi) for good advices and troubleshoots

+ [Radin Shayanfar](https://github.com/radinshayanfar) for pull requests and bug fixes
