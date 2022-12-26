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
url="https://www.youtube.com/watch?v=oNcs95JtUUM"
driver.get(url)


# In[5]:


comments=[]
comment=driver.find_elements(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[2]/ytd-comment-renderer/div[3]/div[2]/div[2]/ytd-expander/div/yt-formatted-string')
for x in comment:
    comments.append(x.text)
print(len(comments),comments)


# In[6]:


upvote=[]
vote=driver.find_elements(By.XPATH,'//span[@class="style-scope ytd-comment-action-buttons-renderer"]')
for x in vote:
    upvote.append(x.text)
print(len(upvote),upvote)


# In[7]:


time=[]
tm=driver.find_elements(By.XPATH,'//a[@dir="auto"]')
for x in tm:
    time.append(x.text)
print(len(time),time)


# In[8]:


for i in range(0,40):
    if i%2==0:
        time.insert(i,'-')
    else:
        continue


# In[9]:


print(len(time),time)


# In[12]:


df=pd.DataFrame()
df['Comments']=comments[0:10]
#df['Up Vote']=upvote[0:20]
df['Time of Comments']=time[0:10]
df


# In[ ]:





# In[ ]:




