#!/usr/bin/env python
# coding: utf-8

# In[9]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[10]:


driver=webdriver.Chrome(r"C:\Users\vgoda\chromedriver.exe")


# In[11]:


driver.maximize_window()


# In[12]:


driver.get('https://www.amazon.in/')
time.sleep(5)


# In[13]:


search_bar=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]') 
search_bar.send_keys ('Laptop')


# In[14]:


search_bar.click()


# In[15]:


search_btn=driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
search_btn.click()


# In[16]:


sfilter=driver.find_element(By.XPATH,'//*[@id="p_n_feature_thirteen_browse-bin/12598163031"]/span/a/span')
sfilter.click()


# In[21]:


title=[]
Scrap_title = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in range(0,10):
    title.append(Scrap_title[i].text)
title


# In[22]:


price=[]
Scrap_price = driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in range(0,10):
    price.append(Scrap_price[i].text)
price


# In[32]:


#scrape first 10 laptops data # Ratings
Ratings=[]
ratings_box = driver.find_elements(By.XPATH,'//div[@class="a-row a-size-small"]')
for i in range(0,10):
   Ratings.append(ratings_box[i].text)
Ratings


# In[33]:


len(price),len(title),len(Ratings)


# In[34]:


df = pd.DataFrame()
df['title'] = title
df['price'] = price
df['Ratings'] = Ratings

df.head(10)


# In[ ]:





# In[ ]:




