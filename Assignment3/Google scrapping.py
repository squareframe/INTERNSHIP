#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from selenium.common.exceptions import ElementClickInterceptedException


# In[2]:


#Let's first connect to web driver
driver = webdriver. Chrome (r"C:\Users\vgoda\chromedriver.exe")
#Let's maximize the automated chrome window
driver.maximize_window()
#Opening up naukri.com website on automated chrome window
url = ('https://images.google.com/')
driver.get(url)


# In[7]:


def search():
    Search_tag=driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search_input=str(input('Type here and I will get you there   ')) # take the user inpute
    Search_tag.send_keys(search_input)
    time.sleep(5)
    search=driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div')
    search.click()
    #Scroll to the end of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)#sleep_between_interactions


# In[8]:


search()


# In[6]:


imgResults = driver.find_elements(By.XPATH,'//img[@data-ils="4"]')
totalResults=len(imgResults)


# In[9]:


totalResults


# In[ ]:


img_urls = set()
for i in  range(0,len(imgResults)):
    img=imgResults[i]
    try:
        img.click()
        time.sleep(2)
        actual_images = driver.find_elements(By.CSS_SELECTOR,'img.n3VNCb')
        for actual_image in actual_images:
            if actual_image.get_attribute('src') and 'https' in actual_image.get_attribute('src'):
                img_urls.add(actual_image.get_attribute('src'))
    except ElementClickInterceptedException or ElementNotInteractableException as err:
        print(err)

