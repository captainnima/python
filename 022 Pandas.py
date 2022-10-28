#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pandas is an external library for data mining
#it can also be used for machine learing

import pandas as pd


# In[2]:


#pandas series

s = pd.Series([1,4,9,16,25,49])


# In[3]:


s


# In[5]:


m = [1,4,9,16,25,49]
m


# In[6]:


s.values


# In[7]:


s[1:3]


# In[8]:


n = pd.Series(['Math', 'History', 'Art', 'English', 'Government'])
n


# In[9]:


n[1:3]


# In[10]:


courses = pd.Series(['Math', 'History', 'Art', 'English', 'Government'], index=['m','h','a','e','g'])
courses


# In[11]:


courses['h':'e']


# In[12]:


courses = pd.Series(['Math', 'History', 'Art', 'English', 'Government'], index=[0,1,2,3,4])
courses


# In[13]:


courses[1:3]


# In[14]:


pop2021 = pd.Series([100,99,97,96,94,89,87], 
                    index=['Python', 'C#', 'Java', 'php', 'C++', 'C', 'Ruby'])


# In[15]:


pop2021


# In[17]:


pop2022 = pd.Series([100,96,94,89,86,77,72], 
                    index=['Python', 'C#', 'Java', 'php', 'C++', 'C', 'Ruby'])


# In[18]:


pop2022


# In[19]:


pop2022[2:5]


# In[20]:


pop2022['Java':'C++']


# In[21]:


#pandas data frames

two_years = pd.DataFrame({'2021': pop2021, '2022': pop2022})


# In[22]:


two_years


# In[23]:


#index lookup using numeric position with iloc

two_years.iloc[0:2]


# In[26]:


#lookup using actual index values with loc

two_years.loc['Python':'C#']


# In[27]:


#use ix which is deprecated
#first parameter is the row indexer and second is the column indexer

two_years.ix[:, ['2022']]


# In[29]:


two_years.loc[:, ['2022']]


# In[31]:


two_years.loc[:, '2022']


# In[ ]:




