# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:10:47 2019

@author: 10541
"""

def replace_latest_slice(query):
    result = ''
    table_list = re.findall(r'latest_slice::(.*?) ', query)
    
    for i in table_list:
        search_term = 'latest_slice::{}'.format(i)
        replace_term = "(SELECT * FROM {} WHERE ds = 'LATEST')".format(i)
        result = query.replace(search_term,replace_term)
        query = result
    return result

import re


query="""SELECT * FROM
latest_slice::sale_order so INNER JOIN latest_slice::res_partner rp ON
so.id = rp.id"""

update_query = replace_latest_slice(query=query)