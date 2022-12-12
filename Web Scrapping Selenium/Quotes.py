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

# Navigate to the website's URL
driver.get('https://www.azquotes.com/')


# In[3]:


Click_on_Top_Quotes=driver.find_element(By.XPATH,'//*[@id="menu"]/div/div[3]/ul/li[5]/a')
Click_on_Top_Quotes.click()


# In[4]:


Quote  =[]
Author=[]
Type=[]


# In[ ]:


driver.close()


# In[5]:


start=0
end=5
for page in range (start, end) :
    SQ=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for a in SQ:
        Quote.append(a.text)
    SA=driver.find_elements(By.XPATH,'//div[@class="author"]') 
    for b in SA:
        Author.append(b.text)
    ST = driver.find_elements(By.XPATH,'//div[@class="tags"]') 
    for c in ST:
        Type.append(c.text)
    driver.find_element(By.XPATH,'//li[@class="next"]').click()
    time.sleep(10)


# In[6]:


driver.find_element(By.XPATH,'//li[@class="next"]').click()


# In[7]:


len(Quote),len(Author),len(Type)


# In[8]:


df = pd.DataFrame()
df['Quote'] = Quote
df['Author']= Author
df['Type'] = Type

df.head(100)


# In[ ]:




