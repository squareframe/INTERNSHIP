#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get("https://presidentofindia.nic.in/former-presidents.htm")


# In[4]:


page


# In[5]:


page.content


# In[6]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[17]:


scraped_Names= soup.find_all('div', 'h3', class_="presidentListing")
scraped_Names


# In[20]:


Names=[]
for Name in scraped_Names:
    Names.append(Name.get_text().replace('\n',''))
    
Names


# In[21]:


import pandas as pd
df = pd.DataFrame()
df['PRESIDENT NAME', 'DOB', 'TERM'] = Names

df


# In[ ]:




