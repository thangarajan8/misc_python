# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:50:07 2019

@author: 10541
"""
def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result
import os
from gensim import corpora, models

import pandas as pd
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import nltk
nltk.download('wordnet')
np.random.seed(2018)
from pathlib import Path
pwd = Path(__file__).resolve().parent
os.chdir(pwd)
stemmer = SnowballStemmer('english')
data = pd.read_csv('abcnews-date-text.csv', error_bad_lines=False);
data_text = data[['headline_text']]
data_text['index'] = data_text.index
documents = data_text


doc_sample = documents[documents['index'] == 4310].values[0][0]
print('original document: ')
words = []
for word in doc_sample.split(' '):
    words.append(word)
print(words)
print('\n\n tokenized and lemmatized document: ')
print(preprocess(doc_sample))

processed_docs = documents['headline_text'].map(preprocess)
pd = processed_docs[:10]

#word_dict = {}
#counter = 0
#for i in pd:
#    for j in i:
#        word_dict[counter] = j
#        counter += 1
    

dictionary = gensim.corpora.Dictionary(processed_docs)
for k,v in dictionary.iteritems():
    print(k,v)
    if k >= 10:
        break

dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)

bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]\


tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]

v = []
for i  in processed_docs:
    for j in i:
      if j == 'broadcast':
          v.append(j)
          
lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=10, id2word=dictionary, passes=2, workers=2)
for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))      