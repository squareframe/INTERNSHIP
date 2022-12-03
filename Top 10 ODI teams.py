#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")


# In[4]:


page


# In[5]:


page.content


# In[6]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[7]:


scraped_teams= soup.find_all(class_="u-hide-phablet")
scraped_teams


# In[8]:


teams=[]
for Team in scraped_teams:
    teams.append(Team.get_text().replace('\n',' '))
    
teams


# In[18]:


scraped_matches= soup.find_all('td', class_='table-body__cell u-center-text')
scraped_matches


# In[19]:


matches=[]
for match in scraped_matches:
    matches.append(match.get_text().replace('\n',""))
    
matches


# In[20]:


scraped_ratings= soup.find_all('td', class_='table-body__cell u-text-right rating')
scraped_ratings


# In[27]:


ratings=[]
for rating in scraped_ratings:
    ratings.append(rating.get_text().replace('\n',''))
    
ratings


# In[29]:


import pandas as pd
df = pd.DataFrame()
df['Teams'] = teams
df['Matches and points']=matches
df['Ratings']=ratings
df


# In[ ]:




