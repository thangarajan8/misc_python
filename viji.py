# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:21:03 2019

@author: Thangarajan
"""

def check_exists_by_xpath(xpath):
    print('checking')
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
from selenium.common.exceptions import NoSuchElementException        
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome('chromedriver.exe')

url = """https://www.amazon.in/s?i=electronics&bbn=1389432031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cp_89%3AApple&pf_rd_i=1389401031&pf_rd_i=symphonypreview&pf_rd_m=A1K21FY43GMZF8&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=8e5e101d-b2f9-4bc4-8ddd-6a7a84807a26&pf_rd_p=previewPlacement_center-1&pf_rd_r=1ZZNESAAV3JSHZGP7D8C&pf_rd_r=ET1D293JP6B6WPAY96V1&pf_rd_s=center-1&pf_rd_s=merchandised-search-leftnav&pf_rd_t=101&pf_rd_t=28601&ref=s9_acss_bw_ln_x_3_2_w"""
first_page = True
data = []
driver.get(url)
time.sleep(5)
html_content = driver.page_source
soup = BeautifulSoup(html_content,'html.parser')
products = soup.find_all('span',{"class":"a-size-medium a-color-base a-text-normal"})
product_price = soup.find_all('span',{"class":"a-price-whole"})
for i,j in zip(products,product_price):
    data.append([i.text,int(j.text.replace(',',''))])
while True:
    if check_exists_by_xpath('//li[@class="a-last"]'):
        next_elem = driver.find_element_by_xpath('//li[@class="a-last"]')
        next_elem.click()
        time.sleep(5)
        print(driver.current_url)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content,'html.parser')
        products = soup.find_all('span',{"class":"a-size-medium a-color-base a-text-normal"})
        product_price = soup.find_all('span',{"class":"a-price-whole"})
        for i,j in zip(products,product_price):
            data.append([i.text,int(j.text.replace(',',''))])
    else:
        break

driver.close()
df = pd.DataFrame(data,columns = ['product','price'])
df.to_csv('apple.csv',index=False, encoding='utf-8')
