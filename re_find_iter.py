# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:59:04 2019

@author: Thanga
"""

import re

from string import *

text_input = """
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
"""

pattern = r'\#(([0123456789abcdefABCDEF0123456789abcdefabcdef])*?)([;,)])'

match = re.findall(pattern,text_input)
[ '#'+i[0] for i in match]
