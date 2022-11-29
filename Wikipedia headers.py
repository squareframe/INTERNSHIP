#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


page = requests.get("https://en.wikipedia.org/wiki/Main_Page")


# In[6]:


page


# In[7]:


soup = BeautifulSoup(page.content)
soup


# In[13]:


first_title=soup.find(class_="mw-headline")
first_title


# In[9]:


first_title.text


# In[12]:


headers=[]


# In[14]:


for i in soup.find_all(class_="mw-headline"):
    headers.append(i.text)
    
headers


# In[ ]:




