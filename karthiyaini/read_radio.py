# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:32:56 2019

@author: Thanga
"""

import win32com.client as win32

f = r"D:\Learning\misc_python\karthiyaini\sample_book.xlsx"
xl = win32.gencache.EnsureDispatch('Excel.Application')
wb = xl.Workbooks.Open(f)
ws = wb.Worksheets.Item(1)
print('Shape count: %s' % len(ws.Shapes))

