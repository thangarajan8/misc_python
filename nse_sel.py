# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:39:09 2020

@author: Thanga
"""

import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#https://www1.nseindia.com/products/content/equities/equities/eq_security.htm
#url = "https://www.nseindia.com/"
url = "https://www1.nseindia.com/products/content/equities/equities/eq_security.htm"
driver = webdriver.Chrome('D:\SW\chromedriver.exe')
driver.get(url)
import time
time.sleep(5)
driver.find_element_by_id('symbol').click()
driver.find_element_by_id('symbol').send_keys('RELIANCE')
select = Select(driver.find_element_by_id('series'))
select.select_by_visible_text('EQ')


###DISABLETHIS###
#driver.find_element_by_id('rdDateToDate').click()
#driver.find_element_by_id('fromDate').send_keys('01-01-2020')
#driver.find_element_by_id('toDate').send_keys('31-03-2020')

###ENABLE THIS###
driver.find_element_by_id('rdPeriod').click()
select = Select(driver.find_element_by_id('dateRange'))
select.select_by_visible_text('3 months')




