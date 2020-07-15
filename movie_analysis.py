# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 07:25:08 2020

@author: Thanga
"""

def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 

from multiprocessing import Pool
import multiprocessing

from imdb import IMDb
import xmltodict, json
from pymongo import MongoClient
client = MongoClient()
db = client['imdb']
col = db['movie']
i = 0
docs = col.find()
d = []
for doc in docs:
    i += 1
    try:
        if doc['movie']['fetch'] == False:
            d.append(doc)
    except Exception:
        raise
    if i % 10000:
        print(i)

ia = IMDb()
id_lst = [str(i).zfill(7) for i in range(1,9999999)]
id_balance = Diff(id_lst,d)
print('Balace {}'.format(len(id_balance)))
#chunks = [id_lst[x:x+100] for x in range(0, len(id_lst), 100)]
print('List Prepared {}'.format(id_lst.__len__()))

    
def api_call(imdb_id):
    print('Processing {}'.format(imdb_id))
    try:
        movie = ia.get_movie(imdb_id)
        o = xmltodict.parse(movie.asXML())
        d = json.loads(json.dumps(o))
        col.insert_one(d)
    except Exception:
        print('FETCH ERROR : {}'.format(imdb_id))
        x = {'movie':{'@id':imdb_id,'fetch':False}}
        col.insert_one(x)
        pass


if __name__ == '__main__':
    p = Pool(multiprocessing.cpu_count())
    p.map(api_call, id_balance)
        
client.close()