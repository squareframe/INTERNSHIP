#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")


# In[3]:


page


# In[4]:


page.content


# In[5]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[7]:


scraped_movies= soup.find_all('td',class_="titleColumn")
scraped_movies


# In[12]:


movies=[]
for movie in scraped_movies:
    movies.append(movie.get_text().replace('\n',''))
    
movies


# In[13]:


scraped_ratings= soup.find_all('td',class_="ratingColumn imdbRating")
scraped_ratings


# In[14]:


ratings=[]
for rating in scraped_ratings:
    ratings.append(rating.get_text().replace('\n',""))
    
ratings


# In[37]:


import pandas as pd
df = pd.DataFrame()
df['Movie Names'] = movies
df['Ratings']=ratings
df.head(100)

