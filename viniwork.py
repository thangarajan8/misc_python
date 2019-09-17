# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:40:18 2018

@author: 10541
"""
import pandas as pd
data = ['acclrtr actn corr cr','plate corr aff credit','alrm alt']
df = pd.DataFrame(data,columns=['content'])
d={'acclrtr':'accelerator','actn':'action','corr':'corrosion','cr':'chemical resistant','aff':'affinity','alrm':'alarm','alt':'alternate'}
d2 = {r'(\b){}(\b)'.format(k):r'\1{}\2'.format(v) for k,v in d.items()}
df['text'] = df['content'].replace(d2, regex=True)

