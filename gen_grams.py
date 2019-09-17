# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 19:43:08 2019

@author: 10541
"""

sentence = "I really like python, it's pretty awesome."
from itertools import chain
def get_grams(sentence,start,end):
    words_bag =[]
    sentence = sentence.lower().split()
    for N in range(start,end):
        word_bag = [sentence[i:i+N] for i in range(len(sentence)-N+1)]
        for wb in word_bag:
            words_bag.append(' '.join(wb))
    return words_bag+sentence
wb = get_grams(sentence,2,4)

def n_grams(tokens, n=1):
    """Returns an iterator over the n-grams given a list of tokens"""
    shiftToken = lambda i: (el for j,el in enumerate(tokens) if j>=i)
    shiftedTokens = (shiftToken(i) for i in range(n))
    tupleNGrams = zip(*shiftedTokens)
    return tupleNGrams #

def range_ngrams(tokens, ngramRange=(1,2)):
    """Returns an itirator over all n-grams for n in range(ngramRange) given a list of tokens."""
    return chain(*(n_grams(tokens, i) for i in range(*ngramRange)))

x = list(range_ngrams(sentence.lower().split()))