# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:17:33 2019

@author: Thanga
"""

html_string = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print('-> {} > {}'.format(attr[0],attr[1]))
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

parser.feed(html_string)