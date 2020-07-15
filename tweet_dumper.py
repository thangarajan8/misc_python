#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
from pymongo import MongoClient
client = MongoClient()
db = client['tamil']
col = db['hindu']
#Twitter API credentials
consumer_key="LWrTypAuRTiwsTdVvX3UKhzOA"
consumer_secret="JxAT3XCN0sxJJxIej06KLFUlTPGCL3Zc7vPW243CJ7OIbFbMsR"
access_key="213246586-gimhCXZ6T2fNNFrX88Ueq3YQNelE99DXGqDB5e2C"
access_secret="G2orpfmI2Nuv8mtf1pP6MmLQf4RsFCc59yxkOnqI3Mgc0"

tweets = []

def get_all_tweets(screen_name):
    global tweets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    alltweets = []  
    
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    alltweets.extend(new_tweets)
    
    oldest = alltweets[-1].id - 1
    
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")
        
        new_tweets = api.user_timeline(screen_name = screen_name,count=2000,max_id=oldest)
        
        alltweets.extend(new_tweets)
        
        oldest = alltweets[-1].id - 1
        
        print(f"...{len(alltweets)} tweets downloaded so far")
    
    tweets.extend(alltweets)



get_all_tweets("TamilTheHindu")

links = [ i.entities['urls'][0]['expanded_url'] for i in tweets]

for link in links:
    try:
        col.insert_one({'_id':link,'content':''})
    except Exception:
        pass
    
client.close()