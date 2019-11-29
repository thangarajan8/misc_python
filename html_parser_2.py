# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:56:12 2019

@author: Thanga
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:26:34 2019

@author: Thanga
"""

from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment')
            print(comment)
        else:
            print('>>> Single-line Comment')
            print(comment)
    def handle_data(self, data):
        if data.strip():
            print('>>> Data\n', data.strip())
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
html_string = """
<div>MY data</div>
<!--A single line comment-->
"""
parser.feed(html_string)