#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[3]:


driver.maximize_window()
url="https://www.flipkart.com"
driver.get(url)


# In[4]:


def Lat(x):
    search_bar=driver.find_element(By.XPATH,'//input[@class="_3704LK"]')
    search_bar.send_keys(x)
    search_btn=driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
    search_btn.click()
    time.sleep(10)
    bn=driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]')
    for i in  bn :
        name.append(i.text)
        BN.append(i.text.split(" ")[0])
        CL.append(i.text.split(",")[-2])
    time.sleep(10)
    n=driver.find_elements(By.XPATH,'//ul[@class="_1xgFaf"]')
    for a in  n :
        hh.append(a.text)


# In[5]:


name=[]
BN=[]
CL=[]
hh=[]


# In[6]:


Lat('Oneplus Nord')


# In[9]:


df= pd.DataFrame() # empty df
df['Name'] = name[0:10]
df['Brand']= BN[0:10]
df['Color']=CL[0:10]
df['Storage']= hh[0:10]
df.head(10)


# In[ ]:




