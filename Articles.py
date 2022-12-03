#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")
page


# In[2]:


page.content


# In[3]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[5]:


scraped_titles= soup.find_all(class_='sc-5smygv-0 fIXTHm')
scraped_titles


# In[6]:


titles=[]
for title in scraped_titles:
    titles.append(title.get_text().replace('\n',' '))
    
titles


# In[7]:


scraped_authors= soup.find_all(class_='sc-1w3fpd7-0 dnCnAO')
scraped_authors


# In[8]:


authors=[]
for i in scraped_authors:
    authors.append(i.get_text().replace('\n',' '))
    
authors


# In[9]:


scraped_publish= soup.find_all(class_='sc-1thf9ly-2 dvggWt')
scraped_publish


# In[10]:


publish=[]
for i in scraped_publish:
    publish.append(i.get_text().replace('\n',' '))
    
publish


# In[12]:


import pandas as pd
df = pd.DataFrame()
df['Title'] = titles
df['Authors']= authors
df['Published']=publish
df


# In[ ]:




