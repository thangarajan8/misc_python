# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:27:20 2020

@author: Thanga
"""

import xml.etree.cElementTree as et

with open('sam.xml','r') as f:
    file_content = f.read()
    
tree=et.fromstring(file_content)
