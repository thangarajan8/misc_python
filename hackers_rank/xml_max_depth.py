# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:43:11 2019

@author: Thanga
"""
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    print('I am Called', level)
    global maxdepth
    if  level == maxdepth:
        maxdepth += 1
    for c in elem:
        depth(c,level+1)
                

xml_string = """
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
    <i>
        <k>
            <l></l>
        </k>
    </i>
</feed>
"""
tree = etree.ElementTree(etree.fromstring(xml_string))
depth(tree.getroot(), -1)
print(maxdepth)
