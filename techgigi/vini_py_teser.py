# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:24:34 2019

@author: Thangarajan
"""
def ocr_core(img):
    img = Image.open(img)
    text = pytesseract.image_to_string(img)
    if len(text.strip()) > 0:
        return True
    else:
        return False
    
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

import glob
image_path = ''
images = glob.glob(image_path)
for image in images:
    if ocr_core(image):
        print('Have Content')
    else:
        print('No Content')
