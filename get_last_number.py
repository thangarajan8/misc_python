# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:44:42 2018

@author: 10541
"""
#import re
def get_number(ip):
    result = ''
    for i in range(-1,-(len(ip)),-1):
        if ip[i].isnumeric():
            result = ip[i]+result
        else:
            break
    print(result)
ip1 = 'abc12cffd345sdf32423'
ip2 = 'sf423h32owkw09-/123/042'
get_number(ip2)
#s = ip1
#re.findall('^.*-([0-9]+)$',ip1)
#next(re.finditer(r'\d+$', ip2)).group(0)
