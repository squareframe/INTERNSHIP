#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[3]:


page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[ ]:





# In[21]:


First_title=soup.find('a',class_="restnt-name ellipsis")
First_title.text


# In[22]:


name=[]


# In[23]:


for i in soup.find_all(class_="restnt-name ellipsis"):
    name.append(i.text)
    
name


# In[24]:


loc=soup.find('div',class_="restnt-loc ellipsis")
loc.text


# In[25]:


loc=[]


# In[26]:


for i in soup.find_all(class_="restnt-loc ellipsis"):
    loc.append(i.text)
    
loc


# In[37]:


img=soup.find('img',class_="no-img")
img


# In[40]:


img=[]
for i in soup.find_all(class_="no-img"):

    img.append(i.get('data-src'))
    
img


# In[ ]:





# In[41]:


rating=soup.find('div',class_="restnt-rating rating-4")
rating.text


# In[43]:


rating=[]
for i in soup.find_all(class_="restnt-rating rating-4"):
    rating.append(i.text)
    
rating


# In[44]:


cuisine=soup.find('span',class_="double-line-ellipsis")
cuisine.text.split('|')[1]


# In[46]:


cuisine=[]
for i in soup.find_all(class_="double-line-ellipsis"):

    cuisine.append(i.text.split('|')[1])
    
cuisine


# In[47]:


import pandas as pd


# In[48]:


df=pd.DataFrame({'Restaurent Name':name,'Cuisine':cuisine,'Location':loc,'Ratings':rating,'Image URL':img})
df


# In[ ]:




