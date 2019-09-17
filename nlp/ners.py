# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:43:12 2019

@author: 10541
"""

import spacy
import pandas as pd
nlp = spacy.load("en_core_web_sm")

f= open('sample.txt','r')
text = f.read()
doc = nlp(text)

ents=[]

for ent in doc.ents:
    #print(ent.label_)
    dictionary={'actual':ent.text,'pred':ent.label_}
    if ent.label_ in  ['GPE','LOC']:
        ents.append([ent.text,ent.label_])
   #pd.DataFrame(data=ent.text, columns='actual')
    print(ent.text, ent.label_)
df = pd.DataFrame(ents,columns=['term','entity'])    
