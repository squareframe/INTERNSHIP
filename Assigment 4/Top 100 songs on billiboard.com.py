#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import needed libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')

#exceptions
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException


# In[2]:


#open web driver

driver=webdriver.Chrome(r"C:\Users\vgoda\chromedriver.exe")
driver.get('https://www.billboard.com/')
driver.maximize_window()


# In[3]:


#open charts
charts=driver.find_element_by_xpath('/html/body/div[3]/header/div[1]/div/div/div[2]/div/nav/ul/li[1]/a')
try:
    charts.click()
except ElementNotInteractableException:#handling element not clickable exception
    driver.get(charts.get_attribute('href'))


# In[ ]:


#open Hot 100 page
hot=driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/span/a')
try:
    hot.click()
except ElementNotInteractableException:#handling element not clickable exception
    driver.get(hot.get_attribute('href'))


# In[4]:


#scrape song name
name=[]
try:
    names=driver.find_elements_by_xpath('//li[@class="lrv-u-width-100p"]/ul/li/h3')
    for x in names:
        name.append(x.text)
except NoSuchElementException:
    name.append('-')
except StaleElementReferenceException:
    name.append('-')
print(len(name),name)


# In[5]:


#scrape Artist name
artist=[]
try:
    artists=driver.find_elements_by_xpath('//li[@class="lrv-u-width-100p"]/ul/li[1]/span[1]')
    for x in artists:
        artist.append(x.text)
except NoSuchElementException:
    artist.append('-')
except StaleElementReferenceException:
    artist.append('-')
print(len(artist),artist)


# In[6]:


#scrape Last week rank
rank=[]
try:
    ranks=driver.find_elements_by_xpath('//li[@class="lrv-u-width-100p"]/ul/li[4]/span')
    for x in ranks:
        rank.append(x.text)
except NoSuchElementException:
    rank.append('-')
except StaleElementReferenceException:
    rank.append('-')
print(len(rank),rank)


# In[7]:


#scrape Peak rank
peak=[]
try:
    peaks=driver.find_elements_by_xpath('//li[@class="lrv-u-width-100p"]/ul/li[5]/span')
    for x in peaks:
        peak.append(x.text)
except NoSuchElementException:
    peak.append('-')
except StaleElementReferenceException:
    peak.append('-')
print(len(peak),peak)


# In[8]:


#scrape Weeks on board
board=[]
try:
    boards=driver.find_elements_by_xpath('//li[@class="lrv-u-width-100p"]/ul/li[6]/span')
    for x in boards:
        board.append(x.text)
except NoSuchElementException:
    board.append('-')
except StaleElementReferenceException:
    board.append('-')
print(len(board),board)


# In[10]:


#make dataframe
df=pd.DataFrame()
df['Song name']=name
df['Artist name']=artist
df['Last week rank']=rank
df['Peak rank']=peak
df['Weeks on board']=board
df


# In[ ]:


#make csv file
df.to_csv('top 100 songs on billiboard.csv')


# In[ ]:


#close the driver
driver.close()

