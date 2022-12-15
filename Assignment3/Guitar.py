#!/usr/bin/env python
# coding: utf-8

# In[12]:


#import required libraries
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


# In[13]:


#connect to driver
driver=webdriver.Chrome(r"C:\Users\vgoda\chromedriver.exe")
driver.maximize_window() #to maximize opened window
driver.get('https://www.amazon.in/') #Opening up amazon.com website on automated chrome window

## Write a python program which searches all the product under a particular product from www.amazon.in.
The product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search
for guitars.
# In[14]:


search_bar=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]') 
search_bar.send_keys ('Guitar') #take user input
search_bar.click()
search_btn=driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
search_btn.click()


# In[4]:


Brand_Name=[] # create a empty list to store the brand name 
Name_of_the_Product=[]
Price=[]
ET=[]


# In[5]:


BN = driver.find_elements(By.XPATH, '//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]')
for i in BN:
    if i.text is None: #if any of the details are missing for any of the product then replace it by “-“.
        Brand_Name.append('-')
    else:
        Brand_Name.append(i.text.split(" ")[0])
for i in BN:
    if i.text is None:
        Name_of_the_Product.append('-')
    else:   
        Name_of_the_Product.append(i.text)
Time = driver.find_elements(By.XPATH,'//span[@class="a-color-base a-text-bold"]')
for i in Time:
    if i.text is None:
        ET.append('-')
    else:
        ET.append(i.text)
p = driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
for i in p:
    if i.text is None:
        Price.append('-')
    else:
        Price.append(i.text)


# In[6]:


len(Brand_Name),len(Name_of_the_Product),len(Price),len(ET)


# In[9]:


Brand_Name=[]
Name_of_the_Product=[]
Price=[]
ET=[]
start=0
end=2
for page in range(start,end):
    brand_tags1=driver.find_elements(By.XPATH, '//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]')
    for i in brand_tags1:
        Brand_Name.append(i.text)
    Name_of_the_Product_tag1=driver.find_elements(By.XPATH,'//span[@class="a-color-base a-text-bold"]')
    for i in Name_of_the_Product_tag1:
        Name_of_the_Product.append(i.text)
    price_tags1=driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
    for i in price_tags1:
        Price.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    next_button.click()
    time.sleep(3)


# In[ ]:





# In[31]:


df=pd.DataFrame()
df['Price']=Price[0:120]
df['Name_of_the_Product']=Name_of_the_Product[0:120]
##df['ET']=ET[0:60]
df['Brand_Name']=Brand_Name[0:120]

df.head(120)


# In[32]:


df.to_csv('guitar.csv')


# In[ ]:




