# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 14:16:00 2022

@author: User
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


driver=webdriver.Chrome('C:/Users/User/web_scrape/chromedriver.exe')
driver.get('https://lf2022.mapyourshow.com/8_0/explore/exhibitor-alphalist.cfm#/')
time.sleep(3)

load_more=driver.find_element_by_xpath('//*[@class="btn-secondary"]')
load_more.click()
time.sleep(3)
load_more.click()
time.sleep(3)
card=driver.find_element_by_xpath('//*[@class="searchResultWrapper"]')
items=card.find_elements_by_xpath('//li[contains(@class,"js-Card")]')

df=pd.DataFrame(columns=['Name','Phone','Address','Description','Website','Social Media'])
i=28
while i<len(items):
    items=card.find_elements_by_xpath('//li[contains(@class,"js-Card")]')
    time.sleep(1)
    try:
        items[i].click()
        time.sleep(6)
        try:
            items[i].click()
        except:
            pass
        
        name_place=driver.find_element_by_xpath('//div[@class="flex  items-center  mb3  mb0-m  flex-wrap"]')
        name=name_place.find_element_by_xpath('//h1').text
        
        contacts=driver.find_element_by_xpath('//section[@id="scroll-onlinecontacts"]')
        try:
            website=contacts.find_element_by_xpath('//a[@title="Visit our website"]').text
        except:
            website=''
        try:
            phone=contacts.find_elements_by_xpath('//li[@class="dib  ml3  mr3"]')[-1].text.split(':')[-1]
        except:
            phone=''
        try:
            address=contacts.find_element_by_xpath('//p[@class="showcase-address  tc"]').text
        except:
            address=''
        
        try:
            des=driver.find_element_by_xpath('//p[@class="js-read-more animated"]').text
        except:
            des=''
    
        try:
            socials=driver.find_element_by_xpath('//div[@class="showcase-social  center  tc"]')
            try:
                twitter=socials.find_element_by_xpath('//a[contains(@title,"Twitter")]').get_attribute("href")
            except:
                twitter=''
            try:
                linkedin=socials.find_element_by_xpath('//a[contains(@title,"LinkedIn")]').get_attribute("href")
            except:
                linkedin=''
            try:
                fb=socials.find_element_by_xpath('//a[contains(@title,"Facebook")]').get_attribute("href")
            except:
                fb=''
            
        except:
            twitter=''
            fb=''
            linkedin=''
    
        
        social={'Facebook':fb,'Twitter':twitter,'LinkedIn':linkedin}
        df=df.append({'Name':name,'Phone':phone,'Address':address,'Description':des,'Website':website,'Social Media':social},ignore_index=True)
        time.sleep(1)
    
        driver.back()
        i=i+1
        time.sleep(8)
    except:
        i+=1


df.to_csv('lightfair.csv',encoding='utf_8_sig',index=False)


