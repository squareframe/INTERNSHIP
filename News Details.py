#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.cnbc.com/world/?region=world")
page


# In[3]:


page.content


# In[4]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[10]:


scraped_headline= soup.find_all(class_='LatestNews-headline')
scraped_headline


# In[11]:


headline=[]
for i in scraped_headline:
    headline.append(i.get_text().replace('\n',' '))
    
headline


# In[7]:


scraped_time= soup.find_all(class_='LatestNews-timestamp')
scraped_time


# In[8]:


time=[]
for i in scraped_time:
    time.append(i.get_text().replace('\n',' '))
    
time


# In[17]:


import pandas as pd
df = pd.DataFrame()
df['Headline'] = headline
df['Time']= time
df.head(30)


# In[ ]:




