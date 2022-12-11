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


# In[3]:


driver=webdriver.Chrome("chromedriver_win32")
driver.get("https://www.flipkart.com/")


# In[4]:


Product=driver.find_element(By.CLASS_NAME,"_3704LK")
Product.send_keys('Sunglasses')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[5]:


brandn=[]
product_desc=[]
price=[]


# In[8]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags[0:40]:
    brand=i.text
    brandn.append(brand)
    
product_desc_tag=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in product_desc_tag[0:40]:
    productd=i.text
    product_desc.append(productd)
    
product_tags=driver.find_elements(By.XPATH,'//div[@class="_25b18c"]')
for i in product_tags[0:40]:
    pprice=i.text
    price.append(pprice)


# In[7]:


print(len(brandn),len(product_desc),len(price))


# In[9]:


brandn


# In[10]:


product_desc


# In[11]:


price


# In[13]:



brandn1=[]
product_desc1=[]
price1=[]
start=0
end=2
for page in range(start,end):
    brand_tags1=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_tags1:
        brandn1.append(i.text)
    product_desc_tag1=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in product_desc_tag1:
        product_desc1.append(i.text)
    price_tags1=driver.find_elements(By.XPATH,'//div[@class="_25b18c"]')
    for i in price_tags1:
        price1.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[12]:


len(brandn1)
brandn1


# In[14]:


len(product_desc1)


# In[15]:


product_desc1


# In[16]:


len(price1)
price1


# In[17]:


brandn2=[]
product_desc2=[]
price2=[]


# In[18]:


start=0
end=3
for page in range(start,end):
    brand_tags2=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_tags2:
        brandn2.append(i.text)
    product_desc_tag2=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in product_desc_tag2:
        product_desc2.append(i.text)
    price_tags2=driver.find_elements(By.XPATH,'//div[@class="_25b18c"]')
    for i in price_tags2:
        price2.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[19]:


len(brandn2),len(product_desc2),len(price2)


# In[ ]:


brandn2

