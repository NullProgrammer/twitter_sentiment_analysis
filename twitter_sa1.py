
import tweepy  # Library
from textblob import TextBlob

consumer_key= 'YOUR CONSUMER_KEY'     
consumer_secret= 'YOUR CONSUMER_SECRET KEY'

access_token='ACCESS_TOKEN KEY'
access_token_secret='ACCESS_TOKEN KEY'   # put all keys and access token generated during making apps on twitter.

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('Narendra modi ')


for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
