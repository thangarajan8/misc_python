# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:48:49 2019

@author: 10541
"""
def distance(v1,v2): 
    return abs(v2[0] - v1[0]) + abs(v2[1] - v1[1])
def print_board(places):
    for i in places:
        print(i)
posr = 0
posc = 0
places = [['b', 'd', '-', '-', '-'], 
          ['-', 'd', '-', '-', '-'], 
          ['-', '-', '-', 'd', '-'], 
          ['-', '-', '-', 'd', '-'], 
          ['-', '-', 'd', '-', 'd']]
print_board(places)
moves = []
prince_row = 0
prince_col = 0
g_poss = []
bot_row = posr
bot_col = posc
moves = []
min_distance = 1000
for i in range(len(places)):
    if 'd' in places[i]:
        prince_row = i
        for j in range(len(places[i])):
            if 'd' == places[i][j] :
                prince_col = j
                g_poss.append([prince_row,prince_col])
#                print(places[i])
val = 'd'
#print([(index, row.index(val)) for index, row in enumerate(places) if val in row])
print(g_poss)
for g_pos in g_poss:
    dist = distance([posr,posc],g_pos)
    if  min_distance == 0:
        min_distance = dist
    elif dist < min_distance:
        min_distance = dist
        close_garbage_loc = g_pos
#        print(' '.join(g_pos))
        print('\n')                
for g_pos in g_poss:
    pr_br = g_pos[0] - bot_row
    pc_bc = g_pos[1] - bot_col
    if pr_br < 0:
        for a in range(abs(pr_br)):
            # print('UP')
            moves.append('UP')
    if pc_bc < 0:
        for b in range(abs(pc_bc)):
            # print('LEFT')
            moves.append('LEFT')
    if pr_br > 0:
        for a in range(abs(pr_br)):
            # print('DOWN')
            moves.append('DOWN')
    if pc_bc > 0:
        for b in range(abs(pc_bc)):
            # print('RIGHT')
            moves.append('RIGTH')
    moves.append('CLEAN')
    bot_row = g_pos[0]
    bot_col = g_pos[1]
print(moves)
##return moves[0]