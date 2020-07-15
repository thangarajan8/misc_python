# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 17:35:29 2020

@author: Thanga
"""

from imdb import IMDb
import pickle
import imdb
# create an instance of the IMDb class
ia = imdb.IMDb()
fid = 1
data = []
for i in range(1,9999999):
    n = str(i)
    print('Processing {}'.format(n))
    imdb_id = n.zfill(7)
#    sleep(i)
    try:
        movie = ia.get_movie(imdb_id)
        data.append(movie)
    except Exception:
        pass
    if i % 1000 == 0:
        fid_str = str(fid).zfill(5)
        with open('D:\Learning\python\misc_python\imdb_data\imdb_{}.pkl'.format(fid_str), 'wb') as f:
            pickle.dump(data, f)
            fid +=1
        data = []

