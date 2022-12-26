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
url="https://trak.in/india-startup-funding-investment-2015/"
driver.get(url)


# In[3]:


Dates=[]
Company=[]
Industry=[]
Investor_Name=[]
Investment_Type=[]
Amount=[]


# In[4]:


#scraping the company_name 
companies=driver.find_elements(By.XPATH,"//td[@class='column-3']")
for i in companies:
    if i.text is None :
        Company.append("--") 
    else:
        Company.append(i.text)
print(len(Company),Company)


# In[5]:


#scraping the Industry 
Ind=driver.find_elements(By.XPATH,"//td[@class='column-4']")
for i in Ind:
    if i.text is None :
        Industry.append("--") 
    else:
        Industry.append(i.text)
print(len(Industry),Industry)


# In[6]:


#scraping the Dates 
dt=driver.find_elements(By.XPATH,"//td[@class='column-2']")
for i in dt:
    if i.text is None :
        Dates.append("--") 
    else:
        Dates.append(i.text)
print(len(Dates),Dates)


# In[7]:


#scraping the Investor_Name 
IN=driver.find_elements(By.XPATH,"//td[@class='column-7']")
for i in IN:
    if i.text is None :
        Investor_Name.append("--") 
    else:
        Investor_Name.append(i.text)
print(len(Investor_Name),Investor_Name)


# In[8]:


#scraping the Investment_Type 
IT=driver.find_elements(By.XPATH,"//td[@class='column-8']")
for i in IT:
    if i.text is None :
        Investment_Type.append("--") 
    else:
        Investment_Type.append(i.text)
print(len(Investment_Type),Investment_Type)


# In[9]:


#scraping the Amount 
Price=driver.find_elements(By.XPATH,"//td[@class='column-9']")
for i in Price:
    if i.text is None :
        Amount.append("--") 
    else:
        Amount.append(i.text)
print(len(Amount),Amount)


# In[10]:


Funding=pd.DataFrame()
Funding['Company']=Company
Funding['Industry']=Industry
Funding['Investor_Name']=Investor_Name
Funding['Amount Invested']=Amount
Funding['Specification']=Investment_Type
Funding['Dates']=Dates


# In[11]:


Funding


# In[ ]:




