# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:12:42 2019

@author: 10541
"""
def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

def getPolygonCentroid(points):
  centroid = {'x': 0, 'y': 0}
  for _ in points:
      centroid['x'] = _['x']
      centroid['y'] = _['y']
      

  centroid['x'] /= len(points)
  centroid['y'] /= len(points)
  return centroid;

  
import pandas as pd  
poly_points = [1774, 282, 1840, 504, 2131, 507, 2134, 276, 1771, 282]
points = chunkIt(poly_points,len(poly_points)/2)

df = pd.DataFrame(points,columns = ['x','y'])
df_dict = df.to_dict(orient='records')

x = getPolygonCentroid(df_dict)