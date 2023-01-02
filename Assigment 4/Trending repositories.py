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
driver.get('https://github.com/')
driver.maximize_window()


# In[3]:


trending_link=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/nav/ul/li[4]/details/div/ul/li[5]/a')
try:
    trending_link.click()
except ElementNotInteractableException:#handling element not clickable exception
    driver.get(trending_link.get_attribute('href'))


# In[4]:


#Scrape Repository Title
title=[]
try:
    titles=driver.find_elements_by_xpath('//span[@class="text-normal"]')
    for x in titles:
        title.append(x.text.replace(' /',''))
except NoSuchElementException:
    title.append('-')
except StaleElementReferenceException:
    title.append('-')
print(len(title),title)


# In[5]:


#scrape Repository Description
description=[]
try:
    descri=driver.find_elements_by_xpath('//p[@class="col-9 color-fg-muted my-1 pr-4"]')
    for x in descri:
        description.append(x.text)
except NoSuchElementException:
    description.append('-')
except StaleElementReferenceException:
    description.append('-')
print(len(description),description)


# In[6]:


#scarpe Contributors count
contributor=[]
try:
    contributors=driver.find_elements_by_xpath('//div[@class="f6 color-fg-muted mt-2"]/a[1]')
    for x in contributors:
        contributor.append(x.text)
except NoSuchElementException:
    contributor.append('-')
except StaleElementReferenceException:
    contributor.append('-')
print(len(contributor),contributor)


# In[7]:


#make dataframe
df=pd.DataFrame()
df['Repository Title']=title
df['Repository Description']=description
df['Repository Contributors']=contributor
df


# In[ ]:


#make csv file
df.to_csv('trending repositories.csv')

