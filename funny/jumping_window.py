# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 12:05:03 2020

@author: Thanga
"""

from pywinauto import application

app =  application.Application()
app.start("Notepad.exe")