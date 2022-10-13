#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 20:26:07 2022

@author: boximao_cat
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import re
from selenium.common.exceptions import TimeoutException



def find_page(new_url,driver,key,key2):
    page_search=False
    # Search page
   
    driver.get(new_url)
    time.sleep(1.5)
    search_bar=driver.find_element_by_xpath('//input[@id="gs_hdr_tsi"]')
    try:
    # get personal url by name+institute
        search_bar.send_keys(key+' '+key2)
        search_bar.send_keys(Keys.ENTER)
    
    
        if key != driver.find_element_by_xpath('//h3[@class="gs_ai_name"]').text:
            #print('Personal Page not found')
            pass
        else:
            personal_url=driver.find_element(By.XPATH,'//div[@class="gs_ai_t"]//a').get_attribute('href')
            driver.get(personal_url)
            time.sleep(1)
            try:
                try:
                    driver.find_element_by_xpath('//div[@id="gsc_prf_ivh"]//a').click()
                except TimeoutException:
                    return page_search
                time.sleep(1)
                page_search=True
            
            except:
                print('No Link Found')
            
    except:
        print('Page not found!')
    return page_search

def email_search(driver,key2):
    
    email_find=r'''(?:[a-zA-Z0-9\._]+(?:\.[a-zA-Z0-9/._]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@'''+key2
    email_find_2=r'''(?:[a-zA-Z0-9\._]+(?:\.[a-zA-Z0-9/._]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@+[a-za-z0-9._-]+((\.|\s*dot\s*)[a-z]*)+(\.|\s*dot\s*)[a-z]*'''
    email_find_3=r'''(?:[a-zA-Z0-9\._]+(?:\.[a-zA-Z0-9/._]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@+[a-za-z0-9._-]+((\.|\s*dot\s*)[a-z]*)'''
    special_1 = re.compile(r'[a-z0-9\.+-]+(\s+\(at\)\s+)+[a-z0-9\._-]+((\.|\s*dot\s*)[a-z]*)+(\.|\s*dot\s*)[a-z]*', flags=re.IGNORECASE)
    special_2 = re.compile(r'[a-z0-9\.+-]+(\s+\(at\)\s+)+[a-z0-9\._-]+(\.|\s*dot\s*)[a-z]*', flags=re.IGNORECASE)
    special_3 = re.compile(r'[a-z0-9\.+-]+(\s+\[at\]\s+)+[a-z0-9\._-]+((\.|\s*dot\s*)[a-z]*)+(\.|\s*dot\s*)[a-z]*', flags=re.IGNORECASE)
    special_4 = re.compile(r'[a-z0-9\.+-]+(\s+\[at\]\s+)+[a-z0-9\._-]+(\.|\s*dot\s*)[a-z]*', flags=re.IGNORECASE)
    special_5 = re.compile(r'[a-z0-9\.+-]+(\s+\(at\)\s+)+[a-z0-9\._-]+((\.|\s*\(\s*dot\s*\)\s*)[a-z]*)+(\.|\s*\(\s*dot\s*\)\s*)[a-z]*', flags=re.IGNORECASE)
    special_6 = re.compile(r'[a-z0-9\.+-]+(\s+\(at\)\s+)+[a-z0-9\._-]+(\.|\s*\(\s*dot\s*\)\s*)[a-z]*', flags=re.IGNORECASE)
    special_7 = re.compile(r'[a-z0-9\.+-]+(\s+\[at\]\s+)+[a-z0-9\._-]+((\.|\s*\[\s*dot\s*\]\s*)[a-z]*)+(\.|\s*\[\s*dot\s*\]\s*)[a-z]*', flags=re.IGNORECASE)
    special_8 = re.compile(r'[a-z0-9\.+-]+(\s+\[at\]\s+)+[a-z0-9\._-]+(\.|\s*\[\s*dot\s*\]\s*)[a-z]*', flags=re.IGNORECASE)
    special_9 = re.compile(r'[a-z0-9\.+-]+(\(at\))+[a-z0-9._-]+((\.|\s*dot\s*)[a-z]*)+(\.|\s*dot\s*)[a-z]*', flags=re.IGNORECASE)
    special_10 = re.compile(r'[a-z0-9\.+-]+(\(at\))+[a-z0-9._-]+(\.|\s*dot\s*)[a-z]*', flags=re.IGNORECASE)
    special_11 = re.compile(r'[a-z0-9\.+-]+(\s*\[at\]\s*)+[a-z0-9\._-]+((\.|\s*\[\s*dot\s*\]\s*)[a-z]*)+(\.|\s*\[\s*dot\s*\]\s*)[a-z]*', flags=re.IGNORECASE)
    special_12 = re.compile(r'[a-z0-9\.+-]+(\s*\[at\]\s*)+[a-z0-9\._-]+(\.|\s*\[\s*dot\s*\]\s*)[a-z]*', flags=re.IGNORECASE)
    special_13 = re.compile(r'[a-z0-9\.+-]+at+[a-z0-9\._-]+(dot[a-z]*)+dot[a-z]*', flags=re.IGNORECASE)
    special_14 = re.compile(r'[a-z0-9\.+-]+at+[a-z0-9\._-]+dot[a-z]*', flags=re.IGNORECASE)
    special_15 = re.compile(r'[a-z0-9\.+-]+(\s+at\s+)[a-z0-9\._-]+((\s*dot\s*)[a-z]*)+(\s*dot\s*)[a-z]*', flags=re.IGNORECASE)
    special_16 = re.compile(r'[a-z0-9\.+-]+(\s+at\s+)[a-z0-9\._-]+(\s*dot\s*)[a-z]*', flags=re.IGNORECASE)
    special_17 = re.compile(r'[a-z0-9\.+-]+(\s+at\s+)[a-z0-9\._-]+((\.)[a-z]*)+(\.)[a-z]*', flags=re.IGNORECASE)
    special_18 = re.compile(r'[a-z0-9\.+-]+(\s+at\s+)[a-z0-9\._-]+(\.)[a-z]*', flags=re.IGNORECASE)


    try:    
        page_source=driver.page_source
    except TimeoutException:
        return 'Timeout'
    list_of_email=[]
    
    for match in re.finditer(email_find,page_source):
        list_of_email.append(match.group())
        break
    if len(list_of_email)==0:
        for m in re.finditer(email_find_2,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(email_find_3,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_1,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_2,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_3,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_4,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_5,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_6,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_7,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_8,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_9,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_10,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_11,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_12,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_13,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_14,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_15,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_16,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_17,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)==0:
        for m in re.finditer(special_18,page_source):
            list_of_email.append(m.group())
            break
    if len(list_of_email)>0:        
        if len(list_of_email[0])>40:
            list_of_email=[]
    if len(list_of_email)>0:
        if list_of_email[0].count('@')>1:
            list_of_email=[]
    if len(list_of_email)>0:
        if '?' in list_of_email[0]:
            list_of_email=[]
    
    if len(list_of_email)==0:
        list_of_email.append('Not Found')
    
    return list_of_email[0]
    
    

                                                            
                                                            



df=pd.read_csv('C:/Users/User/workspace/professor scrape/professor.csv')
df_2=pd.DataFrame(columns=['Name','Email'])


driver=webdriver.Chrome('C:/Users/User/web_scrape/chromedriver.exe')
for i in range(len(df)):

    key=df['Name'][i]
    
    if type(df['Email Verfication'][i])==str:
        key2=df['Email Verfication'][i].split('at ')[1]
    else:
        key2=''
    
    
    new_url='https://scholar.google.com/citations?hl=zh-TW&view_op=search_authors'
    
    driver.set_page_load_timeout(10)
    
    page_result=find_page(new_url,driver,key,key2)
    if page_result==True:
        email=email_search(driver,key2)
    else:
        email='NA'
        
    df_2=df_2.append({'Name':key,'Email':email},ignore_index=True)
    

df3=df_2[df_2['Email']!='NA']
df3=df3[df3['Email']!='Not Found']

df3.index=range(len(df3))



for i in range(len(df3)):
    df3['Email'][i]=df3['Email'][i].lower()
    df3['Email'][i]=df3['Email'][i].replace(' [at] ','@').replace(' (at) ','@').replace('(at)','@').replace('[at]','@').replace(' at ','@')
    df3['Email'][i]=df3['Email'][i].replace(' [dot] ','.').replace(' (dot) ','.').replace('[dot]','.').replace('(dot)','.').replace(' dot ','.')
    df3['Email'][i]=df3['Email'][i].replace('firstname',df3['Name'][i].split(' ')[0].lower())
    df3['Email'][i]=df3['Email'][i].replace('lastname',df3['Name'][i].split(' ')[-1].lower())
    if df3['Email'][i][-1]=='.':
        df3=df3.drop([i])
    elif df3['Email'][i][-1]=='@':
        df3=df3.drop([i])
    elif '/' in df3['Email'][i]:
        df3=df3.drop([i])
   

df3.to_csv('professor_emails.csv')
