# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:28:48 2021

@author: 5034100
"""
def extract(doc):
    try:
        entity = doc['entities']
        hashtag = entity['hashtags']
        user_mentions = entity['user_mentions']
        created_at = doc['created_at']
        extended_tweet = doc['extended_tweet']['full_text']
        location = doc['location']
        screen_name = doc['screen_name']
        d = {}
        d['user_mention'] = user_mentions
        d['hashtag'] = hashtag
        d['created_at'] = created_at
        d['tweet'] = extended_tweet
        d['location'] = location
        d['tweet_user'] = screen_name
        return screen_name
    except Exception:
        return {}
import pymongo

client = pymongo.MongoClient()

db = client['twt']
collection = db['coro']

docs = collection.find()
clean_docs = [extract(doc) for doc in docs]
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
#
#text = "Nick likes to play football, however he is not too fond of tennis."
#text_tokens = word_tokenize(text)
#
#tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
#
#print(tokens_without_sw)
