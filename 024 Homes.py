#!/usr/bin/env python
# coding: utf-8

# In[32]:


#reading in data about homes

import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')


# In[33]:


#custome settings for pandas to make the output larger

pd.set_option('display.max_rows', 6000)
pd.set_option('display.max_columns', 300)
pd.set_option('display.width', 150)


# In[34]:


#load the data

data = pd.read_csv('zip.csv', sep=',')
data.head()


# In[35]:


data.columns.values


# In[36]:


data.shape


# In[37]:


#check the top 10 values in Metro column

data['Metro'][:10]


# In[38]:


#dc metro area

dc_metro_df = data.loc[data['Metro'] == 'Washington']
dc_metro_df.head()


# In[39]:


dc_metro_df.shape


# In[40]:


#check the first row of dc data

dc_metro_df.iloc[0, :]


# In[41]:


#change RegionName to ZipCode

dc_metro_df = dc_metro_df.rename(columns={'RegionName' : 'ZipCode'})
dc_metro_df.head()


# In[42]:


#what is the ZipCode data type?

dc_metro_df['ZipCode'].dtype


# In[43]:


#convert ZipCode to string

dc_metro_df['ZipCode'] = dc_metro_df['ZipCode'].apply(str)
dc_metro_df['ZipCode'].dtype


# In[44]:


#what is lambda?
#Python's anonymous function
#it does not get a name though it can be assigned to a variable
#it is used in a single location
#can be handy

def func(x):
    return x**2


# In[45]:


func(9)


# In[46]:


g = lambda x: x**2
g(9)


# In[47]:


#combine ZipCode, City, and State columns into a single new column
#call it ZipCity

dc_metro_df['ZipCity'] = dc_metro_df[['ZipCode', 'City', 'State']].apply(lambda x: '-'.join(x), axis=1)

#another way
#dc_metro_df['ZipCode'].astype(str) + '-' +
#dc_metro_df['City'].astype(str) + '-' +
#dc_metro_df['state'].astype(str)


# In[48]:


dc_metro_df.head()


# In[49]:


dc_metro_df.columns.values


# In[50]:


#reorder columns so that ZipCity is the first column

cols = dc_metro_df.columns.values.tolist()
cols


# In[51]:


#rearrange the columns

cols = cols[-1:] + cols[:-1]
cols


# In[52]:


#change the column order in the data frame

dc_metro_df = dc_metro_df[cols]
dc_metro_df.head()


# In[53]:


#some testing

test = data.loc[data['Metro'] == 'Washington']
test


# In[54]:


test = test.loc[test['State'] == 'VA']
test


# In[55]:


#exploring the SizeRank column

dc_metro_df.sort_values(by='SizeRank', ascending=False).head(20)


# In[56]:


#drop the SizeRank column

dc_metro_df.drop('SizeRank', axis=1, inplace=True)
dc_metro_df.head()


# In[57]:


#make sure only DC area zip codes are in the dc_metro_df

dc_metro_df['State'].unique()


# In[58]:


#drop the IN values

dc_metro_df.loc[data['State'] == 'IN']


# In[59]:


dc_metro_df = dc_metro_df.drop([5196, 9969]) #rows so we do not need axis=1


# In[60]:


dc_metro_df['State'].unique()


# In[61]:


#store the list of these unique state values

metro_list = dc_metro_df['State'].unique().tolist()
metro_list


# In[62]:


dc_metro_df.shape


# In[63]:


#prepare for plotting subset of the data frame by state

dc_df = dc_metro_df.loc[dc_metro_df['State'] == 'DC']
dc_df.shape


# In[64]:


md_df = dc_metro_df.loc[dc_metro_df['State'] == 'MD']
md_df.shape


# In[65]:


va_df = dc_metro_df.loc[dc_metro_df['State'] == 'VA']
va_df.shape


# In[66]:


wv_df = dc_metro_df.loc[dc_metro_df['State'] == 'WV']
wv_df.shape


# In[69]:


#prepare set of columns for plotting

columns = cols[0:1] + cols[8:]
columns


# In[70]:


#prepare state by state datasets for plotting

va_plot = va_df[columns]
md_plot = md_df[columns]
dc_plot = dc_df[columns]
wv_plot = wv_df[columns]


# In[71]:


va_plot.head()


# In[77]:


#define a function for plotting

def plot_state(state):
    print(state.shape)
    state = state.set_index('ZipCity')
    state_tr = state.transpose()
    county_list = state_tr.columns.values.tolist()
    
    fig = plt.figure()
    
    ax = fig.add_subplot(111)
    ax.set_xlabel('Year-Month')
    ax.set_ylabel('Median Value Per Squre Foot')
    
    for name in county_list:
        state_tr[name].plot()


# In[79]:


#va_plot.set_index('ZipCity').transpose().columns.values.tolist()


# In[80]:


plot_state(va_plot)
plt.show()


# In[81]:


plot_state(md_plot)
plt.show()


# In[82]:


plot_state(dc_plot)
plt.show()


# In[83]:


plot_state(wv_plot)
plt.show()


# In[ ]:




