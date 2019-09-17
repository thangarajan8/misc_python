# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:40:05 2019

@author: 10541
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.co.in/cmp/Google/reviews'

response = requests.get(url)

content = response.content

content_soup = BeautifulSoup(content,'html.parser')

titles = content_soup.find('div',{"class":"cmp-review-title"})
titles.text
