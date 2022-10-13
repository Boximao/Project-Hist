# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 10:48:10 2022

@author: User
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import re
from selenium.common.exceptions import TimeoutException

#set login email and password
email=''
password=''

#go to website
url='https://mjl.clarivate.com/mjl-beta/search-results'
driver=webdriver.Chrome('C:/Users/User/web_scrape/chromedriver.exe')
driver.get(url)
time.sleep(1.5)

#go to login page
login=driver.find_element_by_xpath('//mat-toolbar[@class="mat-toolbar mat-toolbar-single-row"]//button[@class="cdx-but-xl mat-stroked-button mat-button-base mat-primary ng-star-inserted"]')
login.click()

## login to account
driver.switch_to.frame('loginIframe')
login_email=driver.find_element_by_xpath('//input[@autocomplete="login-email"]')
login_password=driver.find_element_by_xpath('//input[@autocomplete="password"]')
login_email.send_keys(email)
login_password.send_keys(password)
login_password.send_keys(Keys.ENTER)
time.sleep(1)

#back to page for scraping
df=pd.DataFrame(columns=['Title','ISSN','Category'])
driver.get(url)
time.sleep(1.5)


profile_list=driver.find_elements_by_xpath('//mat-sidenav-content[@class="mat-drawer-content mat-sidenav-content"]//div[@class="ng-star-inserted"]//div[@class="ng-star-inserted"]//mat-card')
# will meet anti-scrape validation every 100 item scraped
for i in range(2476):
    for i in range(10):
        driver.find_element_by_xpath(f'/html/body/cdx-app/mat-sidenav-container/mat-sidenav-content/main/can-home-page/div/div/div/mat-sidenav-container/mat-sidenav-content/app-journal-search-results/div[3]/div[{i+1}]/mat-card/mat-card-content[2]/div/div/div/div[2]/button').click()
        time.sleep(2.5)
        title=driver.find_element_by_xpath('//mat-card-header[@class="mat-card-header"]//mat-card-title//b').text
        issn=driver.find_element_by_xpath('//mat-card-content[@class="mat-card-content"]//b[@class="ng-star-inserted"]').text
        category=driver.find_element_by_xpath('//mat-card-content[@class="mat-card-content"]//div[@class="subcard-all"]//tbody[@role="rowgroup"]//tr[@class="mat-row ng-star-inserted"]//td[3]').text
        df=df.append({'Title':title,'ISSN':issn,'Category':category},ignore_index=True)
        driver.back()
        time.sleep(2)
    driver.find_element_by_xpath('//div[@class="ng-star-inserted"]//div[@class="mat-paginator-outer-container"]//button[@aria-label="Next page"]').click()
    time.sleep(2)
    
    
