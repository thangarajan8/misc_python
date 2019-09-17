# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:23:52 2019

@author: Thangarajan
"""


def get_mean_std(img):
    data = []
    img_files = glob.glob('{}*.png'.format(IMG_PATH))
    for img_file in img_files:
        doc = {}
        img = cv2.imread(img_file,0)
        if img is not None:
            img_mean,img_std = np.mean(img),np.std(img)
            doc['img_file'] = img_file
            doc['img_mean'] = img_mean
            doc['img_std'] = img_std
            data.append(doc)
    return data
import numpy as np
import cv2
import glob

IMG_PATH = 'E:\\RD\\thirdeye\\test_data\\group\\'

output = get_mean_std(IMG_PATH)