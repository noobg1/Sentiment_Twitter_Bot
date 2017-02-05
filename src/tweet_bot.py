import tweepy
from time import sleep
#from sentiment_mod import sentiment_utility
from twitter_credentials.py import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='@js_channel').items():
    try:
       print('Tweet by: @' + tweet.user.screen_name)
       print(tweet.text)
       #print(sentiment_utility(tweet.text))
       

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
