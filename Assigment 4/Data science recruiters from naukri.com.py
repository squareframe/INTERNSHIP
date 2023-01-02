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
driver.get('https://www.naukri.com/hr-recruiters-consultants')
driver.maximize_window()


# In[3]:


#scrape the names of recruiters
name=[]
try:
    names=driver.find_elements_by_xpath('//span[@class="fl ellipsis"]')
    for x in names:
        name.append(x.text)
except NoSuchElementException:
    name.append('-')
except StaleElementReferenceException:
    name.append('-')
#removing empty data(rows)
name=name[0:24]
print(len(name),name)


# In[4]:


#scrape designations
designation=[]
try:
    designations=driver.find_elements_by_xpath('//span[@class="ellipsis clr"]')
    for x in designations:
        designation.append(x.text)
except NoSuchElementException:
    designation.append('-')
except StaleElementReferenceException:
    designation.append('-')
#removing empty data(row)
designation=designation[0:24]
print(len(designation),designation)


# In[ ]:


#scrape company name
company=[]
try:
    com=driver.find_elements_by_xpath('//small[@class="ellipsis"]')
    for x in com[0:68:2]:
        company.append(x.text)
except NoSuchElementException:
    company.append('-')
except StaleElementReferenceException:
    company.append('-')
#removing empty data
company=company[0:24]
print(len(company),company)


# In[ ]:


#scrape the location
location=[]
try:
    locations=driver.find_elements_by_xpath('//small[@class="ellipsis"]')
    for x in locations[1:68:2]:
        location.append(x.text)
except NoSuchElementException:
    location.append('-')
except StaleElementReferenceException:
    location.append('-')
#removing empty data
location=location[0:24]
print(len(location),location)


# In[ ]:


#scrape the Skills they hire for
skills=[]
try:
    skill=driver.find_elements_by_xpath('//div[@class="hireSec"]')
    for x in skill:
        skills.append(x.text)
except NoSuchElementException:
    skills.append('-')
except StaleElementReferenceException:
    skills.append('-')
print(len(skills),skills)


# In[ ]:


#make dataframe
df=pd.DataFrame()
df['Recruiter Name']=name
df['Designation']=designation
df['Company']=company
df['Skills they hire for']=skills
df['Location']=location
df


# In[ ]:


#make csv file
df.to_csv('Data science recruiters')
#close the driver
driver.close()

