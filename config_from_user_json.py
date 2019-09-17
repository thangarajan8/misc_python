# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 16:16:56 2018

@author: 10541
"""

def get_db_detials(config_file_path):
    data = None
    if not os.path.exists(config_file_path):
        print('Given config file does not exisits quit')
        quit()

    
    with open(config_file_path) as f:
        data = json.load(f)
    
    host = data['hostname']
    port = data['port']
    user = data['user']
    password = data['password']
    db_name = data['db_name']
    return host,port,user,password,db_name

import sys
import json
import os

if len(sys.argv) < 2:
    print('no congfig file given quit')
    quit()

config_file_path = sys.argv[1]

host,port,user,password,db_name = get_db_detials(config_file_path)
print(host,port,user,password,db_name)
