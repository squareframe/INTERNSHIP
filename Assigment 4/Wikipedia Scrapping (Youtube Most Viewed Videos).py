#!/usr/bin/env python
# coding: utf-8

# ## Scrape the details of most viewed videos on YouTube from Wikipedia.
# ### Url = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos
# #### A) Rank
# #### B) Name
# #### C) Artist
# #### D) Upload date
# #### E) Views

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


driver=webdriver.Chrome(r"C:\Users\vgoda\chromedriver.exe")
driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')
driver.maximize_window()


# In[6]:


#scape video name
name=[]
try:
    names = driver.find_elements(By.XPATH, "//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[2]")
    for i in names:
        name.append(i.text)
except NoSuchElementException:
    name.append('No details available')
except StaleElementReferenceException:
    name.append('No details available')
print(len(name))


# In[4]:


#scape rank of video
rank=[]
try:
    ranks=driver.find_elements(By.XPATH,"//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[1]")
    for i in ranks:
        rank.append(i.text.replace('.',''))
except NoSuchElementException:
    rank.append('No details available')
except StaleElementReferenceException:
    rank.append('No details available')
print(len(rank))


# In[7]:


#scape the name of uploader
Artist=[]
try:
    art=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"][1]/tbody/tr/td[3]')
    for x in art:
        Artist.append(x.text)
except NoSuchElementException:
    Artist.append('No details available')
except StaleElementReferenceException:
    Artist.append('No details available')
print(len(Artist))


# In[8]:


#scape upload date
date=[]
try:
    dates=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"][1]/tbody/tr/td[5]')
    for x in dates:
        date.append(x.text)
except NoSuchElementException:
    date.append('-')
except StaleElementReferenceException:
    date.append('-')
print(len(date))


# In[9]:


#scape number of views
views=[]
try:
    view=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"][1]/tbody/tr/td[4]')
    for x in view:
        views.append(x.text)
except NoSuchElementException:
    views.append('-')
except StaleElementReferenceException:
    views.append('-')
print(len(views))


# In[10]:


#make dataframe
df=pd.DataFrame()
df['Rank']=rank
df['Video Name']=name
df['Artist/Uploader Name']=Artist
df['Upload Date']=date
df['Views(Billions)']=views


# In[11]:


df


# In[12]:


#create CSV file
df.to_csv('most viewed videos on YouTube.csv')


# In[13]:


#close the driver
driver.close()


# In[ ]:




