# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:35:01 2020

@author: Thanga
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from pymongo import MongoClient
cliet = MongoClient()
db = cliet['twt']
col = db['movie']
#consumer key, consumer secret, access token, access secret.
ckey="LWrTypAuRTiwsTdVvX3UKhzOA"
csecret="JxAT3XCN0sxJJxIej06KLFUlTPGCL3Zc7vPW243CJ7OIbFbMsR"
atoken="213246586-gimhCXZ6T2fNNFrX88Ueq3YQNelE99DXGqDB5e2C"
asecret="G2orpfmI2Nuv8mtf1pP6MmLQf4RsFCc59yxkOnqI3Mgc0"
i = 0
class listener(StreamListener):

    def on_data(self, data):
        global i
        try:
            col.insert_one(json.loads(data))
            i += 1
            print(i)
        except Exception:
            pass
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["coronavirus","CoronavirusOubreak"])