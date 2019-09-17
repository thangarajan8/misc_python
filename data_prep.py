# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:49:06 2019

@author: Thangarajan
"""

import numpy as np
import guidedlda
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from pymongo import MongoClient

client = MongoClient()
db = client['sma']
collection = db['consumer_complaints']

data = pd.DataFrame(list(collection.find({},{'complaints':1})))
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(lowercase=True,stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)
text_counts= cv.fit_transform(data['complaints'])
Y = text_counts.todense()

import shorttext
usprez = shorttext.data.inaugural()
