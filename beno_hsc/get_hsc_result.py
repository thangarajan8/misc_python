# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:09:00 2019

@author: 10541
"""


from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.keys import Keys
import pandas as pd
driver = webdriver.Chrome('chromedriver.exe')
dateparse = lambda x: pd.datetime.strptime(x, '%m/%d/%Y')
dfs = []
df = pd.read_csv('hsc.csv')
for _,row in df.iterrows():
    try:
        regno = row['reno']
        dob = row['dob']
        base_url = 'http://tnresults.nic.in/nyrpt.htm'
        columns =['regno','dob','name','subject','mark','SPF','total','PF']
        
        driver.get(base_url)
        
        reg_ip = driver.find_element_by_xpath('//input[@id="regno"]')
        reg_ip.send_keys(regno)
        
        dob_ip = driver.find_element_by_xpath('//input[@id="dob"]')
        dob_ip.send_keys(dob)
        
        dob_ip.send_keys(Keys.ENTER)
        
        page_content = driver.page_source
        
        soup = BeautifulSoup(page_content,'html.parser')
        div = soup.find('div',{'class':'design'})
        table = div.find('table')
        trs = table.find_all('tr')
        y = []
        for tr in trs:
            tds = tr.find_all('td')
            x = []
            for td in tds:
                x.append(str(td.text).encode('ascii', 'ignore'))
#            print(x)
            y.append(x)
        result = []
        student_name = str(y[0][0]).split('(')[0].replace("b'",'')
        total_result = str(y[-1][4]).replace("b'",'').replace("'",'')
        tpf = str(y[-1][5]).replace("b'",'').replace("'",'')
        for i in y[2:8]:
            subject = str(i[0]).replace("b'",'').replace("'",'').strip()
            mark = str(i[4]).replace("b'",'').replace("'",'').strip()
            pf = str(i[5]).replace("b'",'').replace("'",'').strip()
            result.append([regno,dob,student_name,subject,mark,pf,total_result,tpf])
        
        df = pd.DataFrame(result,columns=columns)
#        df.to_csv('{}.csv'.format(regno),index=False)
        dfs.append(df)
    except:
        print(regno)
        pass
driver.close()
d = pd.concat(dfs)
d.to_csv('results.csv',index=False)