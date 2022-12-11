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


driver=webdriver.Chrome("chromedriver_win32")


# In[3]:


driver.get("https://www.flipkart.com/")


# In[4]:


Product=driver.find_element(By.CLASS_NAME,"_3704LK")
Product.send_keys('sneakers')


# In[5]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[6]:


brandn=[]
product_desc=[]
price=[]


# In[9]:


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


# In[10]:


print(len(brandn),len(product_desc),len(price))


# In[11]:


brandn


# In[12]:


product_desc


# In[13]:


price


# In[22]:


brandn1=[]
product_desc1=[]
price1=[]


# In[23]:


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


# In[18]:


len(brandn1)


# In[24]:


brandn2=[]
product_desc2=[]
price2=[]


# In[25]:


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


# In[ ]:


