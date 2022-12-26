#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time

# Set up Selenium and the web driver
driver = webdriver.Chrome(r"C:\Users\vgoda\chromedriver.exe")


# In[2]:


driver.maximize_window()
url="https://www.hostelworld.com/s?q=London,%20England&city=London&country=England&type=city&id=3&from=2022-05-24&to=2022-05-27&guests=2&page=1"
driver.get(url)


# In[3]:


hotel_name=[]
name=driver.find_elements(By.XPATH,'//h2[@class="title title-6"]/a[1]')
for x in name:
    hotel_name.append(x.text)
print(len(hotel_name),hotel_name)


# In[4]:


distance=[]
dis=driver.find_elements(By.XPATH,'//span[@class="description"]')
for x in dis:
    distance.append(x.text)
print(len(distance),distance)


# In[5]:


ratings=[]
rate=driver.find_elements(By.XPATH,'//div[@class="score orange big"]')
for x in rate:
    ratings.append(x.text)
print(len(ratings),ratings)df=pd.DataFrame()
df['Hostel_Name']=hotel_name[0:29]
df['distance from city centre']=distance[0:29]
df['Ratings']=ratings[0:29]
df['Reviews']=reviews[0:29]


# In[6]:


reviews=[]
review=driver.find_elements(By.XPATH,'//div[@class="reviews"]')
for x in review:
    reviews.append(x.text)
print(len(reviews),reviews)


# In[7]:


df=pd.DataFrame()
df['Hostel_Name']=hotel_name[0:29]
df['distance from city centre']=distance[0:29]
df['Ratings']=ratings[0:29]
df['Reviews']=reviews[0:29]


# In[8]:


df


# In[ ]:




