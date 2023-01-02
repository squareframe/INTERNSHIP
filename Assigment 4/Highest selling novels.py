#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[1]:


#open web driver

driver=webdriver.Chrome(r"C:\Users\vgoda\chromedriver.exe")
driver.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare/')
driver.maximize_window()


# In[ ]:


#scrape book name
name=[]
try:
    names=driver.find_elements_by_xpath('//table[@class="in-article sortable"]/tbody/tr/td[2]')
    for x in names:
        name.append(x.text)
except NoSuchElementException:
    name.append('-')
except StaleElementReferenceException:
    name.append('-')
print(len(name),name)


# In[ ]:


#scrape Author name
author=[]
try:
    authors=driver.find_elements_by_xpath('//table[@class="in-article sortable"]/tbody/tr/td[3]')
    for x in authors:
        author.append(x.text)
except NoSuchElementException:
    author.append('-')
except StaleElementReferenceException:
    author.append('-')
print(len(author),author


# In[ ]:


#scrape Volumes sold
sold=[]
try:
    solds=driver.find_elements_by_xpath('//table[@class="in-article sortable"]/tbody/tr/td[4]')
    for x in solds:
        sold.append(x.text)
except NoSuchElementException:
    sold.append('-')
except StaleElementReferenceException:
    sold.append('-')
print(len(sold),sold)


# In[ ]:


#scrape publisher name
publisher=[]
try:
    publishers=driver.find_elements_by_xpath('//table[@class="in-article sortable"]/tbody/tr/td[5]')
    for x in publishers:
        publisher.append(x.text)
except NoSuchElementException:
    publisher.append('-')
except StaleElementReferenceException:
    publisher.append('-')
print(len(publisher),publisher)


# In[ ]:


#scrape Genre name
genre=[]
try:
    genres=driver.find_elements_by_xpath('//table[@class="in-article sortable"]/tbody/tr/td[6]')
    for x in genres:
        genre.append(x.text)
except NoSuchElementException:
    genre.append('-')
except StaleElementReferenceException:
    genre.append('-')
print(len(genre),genre)


# In[ ]:


#make dataframe
df=pd.DataFrame()
df['Book name']=name
df['Author name']=author
df['Volumes sold']=sold
df['Publisher']=publisher
df['Genre']=genre
df


# In[ ]:


#make csv file
df.to_csv('Highest selling novels.csv')
#close the driver
driver.close()

