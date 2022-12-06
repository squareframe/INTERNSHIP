#!/usr/bin/env python
# coding: utf-8

# In[13]:


from bs4 import BeautifulSoup
import requests


# In[14]:


page = requests.get("https://presidentofindia.nic.in/former-presidents.htm")
page


# In[15]:


page.content


# In[16]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[17]:


scraped_Names= soup.find_all('div', 'h3', class_="presidentListing")
scraped_Names


# In[18]:


name = [] # creating empty list

for i in soup.find_all("div",class_="presidentListing"): 

    name.append(i.find("h3").text.split("(")[0])
    
name


# In[19]:


scraped_term = soup.find_all('div', 'p', class_="presidentListing")
scraped_term


# In[20]:


term = [] # creating empty list

for i in soup.find_all("div",class_="presidentListing"): 

    term.append(i.find("p").text.split("(")[0])
    
term


# In[36]:


import pandas as pd
df = pd.DataFrame()


# In[37]:


df['President Name'] = name
df['Term'] = term
df


# In[ ]:





# In[ ]:




