# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 16:34:41 2018

@author: 10541
"""

dev = "dev_odbc_connetion"
test = "test_odbc_connetion"
prod = "prod_odbc_connetion"

import sys


if len(sys.argv) < 2:
    print('no congfig ID given quit')
    quit()

config_id = sys.argv[1]

db_config = None

if config_id == dev:
    db_config = dev


if db_config is None:
    print('Give config id is not available please try a/b/c quiting')
    quit()
else:
    print(db_config)