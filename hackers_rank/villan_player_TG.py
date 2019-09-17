# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:24:44 2019

@author: 10541
"""
villan = "10 20 50 100 500 400"
player = "30 20 60 70 90 490"

villan_str = list(map(int,villan.split(' ')))
player_str = list(map(int,player.split(' ')))

player_sorted = sorted(player_str, reverse=True)
player_win = 0
while len(villan_str) > 0:
#    print('hai')
    max_villan = max(villan_str)
    max_player = max(player_str)
    
    max_villan_index = villan_str.index(max_villan)
    max_player_index = player_str.index(max_player)
    
    print('Player: {} | Villan: {}'.format(max_player,max_villan))
    
    if max_player > max_villan:
        player_win += 1
    
    del villan_str[max_villan_index]
    del player_str[max_player_index]
if len(player_sorted) == player_win:
    print('WIN')
elif len(player_sorted) != player_win:
    print('LOSE')