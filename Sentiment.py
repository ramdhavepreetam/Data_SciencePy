#bag of word 
#register 
# Data_SciencePy
# This is python data Science Code 
# Dependency 1 of 2 
# Install via pip 
# pip install tweepy
# Dependency 2 of 2 
# pip install textblob
import tweepy
from textblob import TextBlob

wiki = TextBlob("Preetam is angry because it is taking some time for him to understand the things and it is slowing him down. ")

consumer_key = '6XpxMkRbWRuZAYEtUiWu1dSnh'
consumer_secret ='MXmk4b5ELxjPwVD6zscAcCSgAesNTujXZiTtgrJ9UUJ50RqCZK'

access_token = '368951424-yvhZVFsnFjUEagtVFzvIeHhYebLOgnx7ZQuXrhnL'
access_token_secret ='61MXQCHZ2QBlXsetDwnMgQcfyVPicNKA3xBQhgznNmIYt'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Tensorflow')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

