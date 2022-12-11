#!/usr/bin/env python
# coding: utf-8

# In[6]:


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

# Navigate to the website's URL
driver.get('https://www.azquotes.com/')

# Find the Top Quotes link
driver.find_element_by_link_text("Top Quotes").click()


# In[5]:


quote = driver.find_elements(By.XPATH,'//div[@class="title"]')
author = driver.find_elements(By.XPATH,'//div[@class="author"]')
type_of_quote = driver.find_elements(By.XPATH,'//div[@class="author"]')


# In[7]:


print(quote)
print(author)
print(type_of_quote)


# In[ ]:


driver.close()


# In[ ]:




