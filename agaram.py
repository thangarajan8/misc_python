# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:31:23 2020

@author: Thanga
"""
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
url = "http://tnresults.nic.in/cdprpt.htm"
binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options = Options()
#options.set_headless(headless=True)
options.binary = binary
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True #optional
driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path="D:\\SW\\geckodriver-v0.26.0-win32\\geckodriver.exe")


df = pd.read_excel('Agaram_+2 Reg. No & DOB.xlsx')
df['dob'] = df.apply(lambda x : datetime.datetime.strftime(x['DOB'],'%d/%m/%Y'),axis=1)
dfs = []
ds = []
for index,row in df.iterrows():
    d = {}
    try:
        driver.get(url)
        reg = row['HSC - 2 \nReg. No']
        reg_ip = driver.find_element_by_id('regno')
        reg_ip.send_keys(row['HSC - 2 \nReg. No'])
        dob = row['dob']
        dob_ip = driver.find_element_by_id('dob')
        dob_ip.send_keys(dob)
        
        submit_button = driver.find_element_by_name('B1')
        submit_button.click()
        
        x = driver.find_element_by_xpath('//div[@class="design"]/table')
        for i in x.text.split('\n'):
            print(i)
            
        df_list = pd.read_html(driver.page_source)
        y = 0
        for dl in df_list:
            print(dl.shape)
            if dl.shape == (9,6):
                y = dl
                dfs.append(dl)
                print(4)
                break
    except Exception:
        d['reg'] = reg
        ds.append(d)
        pass
#driver.find_element_by_id('symbol').click()
#driver.find_element_by_id('symbol').send_keys('RELIANCE')
#select = Select(driver.find_element_by_id('series'))
#select.select_by_visible_text('EQ')
#print ("Headless Firefox Initialized")
##driver.quit()
#driver.find_element_by_id('rdPeriod').click()
#select = Select(driver.find_element_by_id('dateRange'))
#select.select_by_visible_text('3 months')
#
#img = driver.find_element_by_xpath('//a/img')
#img.click()
driver.close()

m = dfs[0]
m

mapping = {0:'Subject',1:'b',2:'c',3:'d',4:'Mark',5:'Pass/Fail'}
dfs1 = [data.rename(columns=mapping)[['Subject','Mark','Pass/Fail']] for data in dfs]
result = []
for l in dfs1:
#l = dfs1[0]
    name_num = l['Subject'].iloc[0]
    name = name_num.split('(')[0].strip()
    num = name_num.split('(')[1].replace(')','').strip()
    mark = int(l[8:]['Mark'])
    l1 = l[2:8]
    l1['name'] = name
    l1['reg_no'] = num
    l1['total'] = mark
    result.append(l1)
final = pd.concat(result)
final.to_csv('result.csv',index=False)
error_df = pd.DataFrame(ds)
error_df.to_csv('error.csv',index=False)
