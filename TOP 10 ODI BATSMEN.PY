#!/usr/bin/env python
# coding: utf-8

# In[14]:


from bs4 import BeautifulSoup
import requests


# In[15]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
page


# In[16]:


page.content


# In[17]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[21]:


scraped_players= soup.find_all('td', class_='table-body__cell rankings-table__name name')
scraped_players


# In[22]:


players=[]
for player in scraped_players:
    players.append(player.get_text().replace('\n',' '))
    
players


# In[23]:


scraped_teams= soup.find_all(class_="table-body__logo-text")
scraped_teams


# In[24]:


teams=[]
for Team in scraped_teams:
    teams.append(Team.get_text().replace('\n',' '))
    
teams


# In[25]:


scraped_ratings= soup.find_all('td', class_='table-body__cell rating')
scraped_ratings


# In[26]:


ratings=[]
for rating in scraped_ratings:
    ratings.append(rating.get_text().replace('\n',''))
    
ratings


# In[28]:


import pandas as pd
df = pd.DataFrame()
df['Players'] = players
df['Teams']= teams
df['Ratings']=ratings
df.head(10)


# In[ ]:




