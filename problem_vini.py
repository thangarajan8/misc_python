# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:44:46 2019

@author: 10541
"""
def ngram(text, ngrams=1):
    tokens = list(text)
    return [''.join(list(tokens[i:i+ngrams])) for i in range(len(tokens)-ngrams+1)]

word = 'abcdef'

word_bag = []
for i in range(2,4):
    word_bag += ngram(word,ngrams=i)
    
sorted(word_bag)
