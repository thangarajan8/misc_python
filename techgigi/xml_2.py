# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:50:28 2019

@author: Thangarajan
"""

import xml.etree.ElementTree as etree

def get_attr_number(node):
    attr_count = len(node.attrib.keys())
    for child in node:
        if len(list(child)) > 0:
            for c in child:
                attr_count += len(child.attrib.keys())
        attr_count += len(child.attrib.keys())
    return attr_count
    # your code goes here

if __name__ == '__main__':
    xml = """<feed xml:lang='en'>
<title>HackerRank</title>
<subtitle lang='en'>Programming challenges</subtitle>
<link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
<updated>2013-12-25T12:00:00</updated>
<entry>
<author gender='male'>Harsh</author>
<question type='hard'>XML 1</question>
<description type='text'>This is related to XML parsing</description>
</entry>
</feed>"""
    at_count = 0
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    at_count += len(root.attrib.keys())
    for child in root:
        if len(list(child)) > 0:
            for c in child:
                at_count += len(c.attrib.keys())
        at_count += len(child.attrib.keys())
#        print(len(child.attrib.keys()))
#    print(get_attr_number(root))