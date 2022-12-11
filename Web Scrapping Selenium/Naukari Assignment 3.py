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


# In[2]:


driver=webdriver.Chrome(r"C:\Users\vgoda\chromedriver.exe")


# In[3]:


driver.get("https://www.naukri.com/")
driver.maximize_window()


# In[4]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[5]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[8]:


job_title=[]
title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title) 


# In[9]:


print(len(job_title))


# In[10]:


df=pd.DataFrame({'job_title':job_title})
df


# In[34]:


location_filter = driver.find_element(By.XPATH,"//*[@id='chk-Delhi / NCR-cityTypeGid-']")
location_filter.click("Delhi / NCR")


# In[35]:


Salary = driver.find_element(By.XPATH,"//*[@id='chk-3-6 Lakhs-ctcFilter-']")
Salary.click('3-6 Lakhs')


# In[36]:


df=pd.DataFrame({'job_title':job_title, 'Location':location_filter, 'Salary':Salary})
df


# In[ ]:




