#!/usr/bin/env python
# coding: utf-8

# In[12]:


from bs4 import BeautifulSoup
import requests


# In[13]:


page = requests.get("https://www.imdb.com/chart/top/")


# In[14]:


page


# In[15]:


page.content


# In[16]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[17]:


scraped_movies= soup.find_all(class_="titleColumn")
scraped_movies


# In[18]:


movies=[]
for movie in scraped_movies:
    movies.append(movie.get_text().replace('\n',""))
    
movies


# In[19]:


scraped_ratings= soup.find_all(class_="ratingColumn imdbRating")
scraped_ratings


# In[20]:


ratings=[]
for rating in scraped_ratings:
    ratings.append(rating.get_text().replace('\n',""))
    
ratings


# In[21]:


import pandas as pd
data = pd.DataFrame()
data['Movie Names'] = movies
data['Ratings']=ratings
data.head(100)


# In[ ]:





# In[ ]:





# In[ ]:




