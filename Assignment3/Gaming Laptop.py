#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[4]:


driver.maximize_window()
url="https://www.digit.in/top-products/best-gaming-laptops-40.html"
driver.get(url)


# In[5]:


Brands              =[]
Products_Description=[]
Specification       =[]


# In[6]:


brand=driver.find_elements(By.XPATH,'//div[@class="TopNumbeHeading"]')
for i in brand:
    Brands.append(str(i.text).replace("\n",""))
Brands


# In[7]:


specification_tag=driver.find_elements(By.XPATH,"//div[@class='Specs-Wrap']")
for i in specification_tag:
    Specification.append(str(i.text).replace("\n",""))
Specification


# In[8]:


description=driver.find_elements(By.XPATH,"//div[@class='Section-center']")
for i in description:
    Products_Description.append(str(i.text).replace("\n",""))
Products_Description


# In[9]:


Price=[]
price_tag=driver.find_elements(By.PARTIAL_LINK_TEXT,"₹ ")
for i in price_tag:
    Price.append(str(i.text).replace("\n","").replace('₹ ',''))
Price


# In[10]:


laptop=pd.DataFrame()
laptop['Brands']=Brands[0:9]
laptop['Price']=Price[0:9]
laptop['Specification']=Specification[0:9]
laptop['Description']=Products_Description[0:9]


# In[11]:


laptop


# In[12]:


laptop.to_csv('laptop.csv')


# In[ ]:




