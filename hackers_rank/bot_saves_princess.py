# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:44:29 2019

@author: 10541
"""

grid = 3
places = ['p--', '-m-', '---']
prince_row = 0
prince_col = 0

bot_row = 0
bot_col = 0

for i in range(len(places)):
    if 'p' in places[i]:
        prince_row = i
        for j in range(len(places[i])):
            if 'p' == places[i][j] :
                prince_col = j
    if 'm' in places[i]:
        bot_row = i
        for k in range(len(places[i])):
            if 'm' == places[i][k] :
                bot_col = k

print('Prince in {} {}'.format(prince_row,prince_col))
print('Bot in {} {}'.format(bot_row,bot_col))

print(prince_row-bot_row)