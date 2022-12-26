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


#Let's maximize the automated chrome window
driver.maximize_window()
url="https://www.forbes.com/billionaires/"
driver.get(url)


# In[3]:


Name=[]
Rank=[]
Net_worth=[]
Citizenship=[]


# In[4]:


name_tag=driver.find_elements(By.XPATH,'//div[@class="personName"]/div[1]')
for x in name_tag:
    Name.append(x.text)


# In[5]:


print(len(Name),Name)


# In[6]:


net=driver.find_elements(By.XPATH,'//div[@class="netWorth"]/div[1]')
for x in net:
    Net_worth.append(x.text.replace('B',' Billion Dollers').replace('$',''))
print(len(Net_worth),Net_worth)


# In[7]:


citizenship=driver.find_elements(By.XPATH,'//div[@class="countryOfCitizenship"]')
for x in citizenship:
    Citizenship.append(x.text)
print(len(Citizenship),Citizenship)


# In[8]:


Source=[]
source=driver.find_elements(By.XPATH,'//div[@class="expand-row__icon-container"]/span[1]')
for x in source:
    Source.append(x.text)
print(len(Source),Source)


# In[9]:


rank_tag=driver.find_elements(By.XPATH,'//div[@class="rank"]')
for x in rank_tag:
    Rank.append(x.text.replace('.',''))
print(len(Rank),Rank)


# In[10]:


billionaires=pd.DataFrame()
billionaires['Rank']=Rank
billionaires['Name']=Name
billionaires['Net Worth']=Net_worth
billionaires['Citizenship/Country']=Citizenship
billionaires['Source']=Source


# In[11]:


billionaires


# In[12]:


billionaires.to_csv('Billionaires.csv')


# In[ ]:




