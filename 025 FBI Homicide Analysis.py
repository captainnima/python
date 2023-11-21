#!/usr/bin/env python
# coding: utf-8

# # 025 FBI Homicide Analysis

# In[1]:


#FBI Homicide

import pandas
import matplotlib.pyplot as plt
from IPython.display import display


# In[2]:


#https://pandas.pydata.org/docs/user_guide/options.html
pandas.set_option('display.notebook_repr_html', True)
pandas.set_option('display.precision', 2)


# In[3]:


#read in the data
totals = pandas.read_csv('totals.csv', sep='\t', index_col=0)
guns = pandas.read_csv('guns.csv', sep='\t', index_col=0)
gdp = pandas.read_csv('gdp.csv', sep='\t', index_col=1)


# In[4]:


totals.head(10)


# In[5]:


guns.head(10)


# In[6]:


gdp.head(10)


# In[7]:


#combine the 3 data frames to form a new data frame
data = totals.join(guns).join(gdp)
data.head()


# In[8]:


#create a new column
data['Gun Percent'] = 100*data['Gun Homicides'] / data['Homicides']
data.head()


# In[9]:


#delete unneeded columns
del data['Unintentional'], data['Undetermined'], data['Gun Suicides']


# In[10]:


data.head()


# In[11]:


#drop NaNs
data = data.dropna()


# In[12]:


data.head()


# In[13]:


import warnings
warnings.filterwarnings('ignore')


# In[14]:


topFive = data.loc[:, ['Homicides', 'Gun Homicides']][:5]


# In[15]:


topFive


# In[16]:


topFive.plot()
plt.show()


# In[17]:


topFive.plot(kind='bar')
plt.show()


# In[18]:


#functions
def plot_percapita(df, limit=10):
    df = df.loc[:, ['Homicides', 'Gun Homicides']][:limit]
    df['Total Homicides'] = df['Homicides'] - df['Gun Homicides']
    del df['Homicides']
    df.plot(kind='bar', stacked=True)
    plt.ylabel('Per 100k')
    plt.show()


# In[23]:


plot_percapita(data, 5)


# In[24]:


def display_relevant(df, limit=10):
    display(df.loc[:, ['Homicides', 'Gun Homicides']][:limit])


# In[25]:


display_relevant(data, 5)


# In[26]:


data['Gun Percent'].plot()
plt.show()


# In[27]:


def plot_percent(df, limit=10):
    df['Gun Percent'][:limit].plot()
    plt.ylim(0, 100)
    plt.title('% Gun Homicide')
    plt.show()


# In[28]:


plot_percent(data, 5)


# In[29]:


top = data.sort_values(by='GDP')
top.head()


# In[30]:


top[-30:]


# In[31]:


top = top[-30:] #top 30 countries by GDP


# In[32]:


top


# In[33]:


top_by_guns = top.sort_values(by='Gun Homicides', ascending=False)
top_by_guns


# In[34]:


display_relevant(top_by_guns, 5)


# In[35]:


plot_percapita(top_by_guns, 10)


# In[ ]:




