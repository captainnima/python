#!/usr/bin/env python
# coding: utf-8

# In[56]:


#mining baby names

import pandas as pd
import matplotlib.pyplot as pp
import zipfile
import os


# In[57]:


#read in the baby names zip file and extract
#extract to the local directory which is desigante by (.)

zipfile.ZipFile('names.zip').extractall('.')


# In[58]:


#view the files

os.listdir('names')[:10]


# In[59]:


#use Python commands to open a file

open('names/yob2011.txt', 'r').readlines()[:10]


# In[60]:


#use Pandas commands to read the same file and assign the results to a variable

names_2011 = pd.read_csv('names/yob2011.txt')
names_2011.head(10)


# In[61]:


#adjust the heading

names_2011 = pd.read_csv('names/yob2011.txt', names=['name', 'sex', 'number'])
names_2011.head(10)


# In[62]:


names_2011.head()


# In[63]:


names_2011.tail()


# In[64]:


#create a new list that contains all the names from all the years;
#add a year column

names_all = []

for year in range(1880, 2014+1):
    names_all.append(pd.read_csv('names/yob{}.txt'.format(year), names=['name', 'sex', 'number']))
    names_all[-1]['year'] = year


# In[65]:


names_all


# In[66]:


#now place all the list elements (data frames) into a single data frame

all_years = pd.concat(names_all)
all_years.head()


# In[67]:


all_years.tail()


# In[68]:


#create a new data frame that is indexed by sex, then by name, theny by year;
#let's sort the data also

all_years_indexed = all_years.set_index(['sex', 'name', 'year']).sort_index()


# In[69]:


all_years_indexed


# In[70]:


#lookup Mary

all_years_indexed.loc['F', 'Mary'].head()


# In[71]:


all_years_indexed.loc['M', 'Joseph'].head()


# In[72]:


all_years_indexed.loc['M', 'Sue'].head()


# In[73]:


#create a function to plot a name

def plot_name(sex, name):
    data = all_years_indexed.loc[sex, name]
    pp.plot(data.index, data.values)


# In[74]:


x = [4,7,8,9]
y = [30, 50, 20, 40]

pp.plot(x, y)
pp.show()


# In[75]:


plot_name('F', 'Mary')
pp.show()


# In[76]:


plot_name('M', 'Joseph')
pp.show()


# In[77]:


#loop through a collection of popular boy names and graph them

pp.figure(figsize=(12, 3))

names = ['Michael', 'John', 'David', 'Joseph']

for name in names:
    plot_name('M', name)
    
pp.legend(names)
pp.show()


# In[78]:


#loop through a collection of popular girl names and graph them

pp.figure(figsize=(12, 3))

names = ['Emily', 'Anna', 'Claire', 'Elizabeth']

for name in names:
    plot_name('F', name)
    
pp.legend(names)
pp.show()


# In[79]:


#loop through a collection of a girl name with different spelling/sound

pp.figure(figsize=(12, 3))

names = ['Kathleen', 'Kathy', 'Cathleen', 'Cathy', 'Kat']

for name in names:
    plot_name('F', name)
    
pp.legend(names)
pp.show()


# In[80]:


names


# In[81]:


all_years_indexed.loc['F'].loc[names]


# In[82]:


#unstack the data frame: unstacking means moving the innermost row index to become
#the innermost column index

all_years_indexed.loc['F'].loc[names].unstack(level=0).head()


# In[83]:


#replace the NaNs with 0

all_years_indexed.loc['F'].loc[names].unstack(level=0).fillna(0).head()


# In[84]:


#popular boy names for 2008

pop_2008 = all_years_indexed.loc['M',:,2008].sort_values(by='number', ascending=False)


# In[85]:


pop_2008.head()


# In[86]:


#reset the default index

pop_2008.reset_index().head(10)


# In[87]:


#drop the unnecessary columns

pop_2008.reset_index().drop(['number'], axis=1).head(10)


# In[88]:


#create a function to return the top names for any year based on gender

def top_names(sex, year, total=10):
    top_list = all_years_indexed.loc[sex,:,year].sort_values(by='number', ascending=False)
    top_list = top_list.reset_index()
    top_list = top_list.drop(['number'], axis=1).head(total)
    top_list.columns = [year]
    top_list.index += 1
    
    return top_list


# In[89]:


top_names('M', 2008, 5)


# In[90]:


top_names('M', 1970)


# In[91]:


top_names('F', 1970)


# In[92]:


years = [top_names('M', year) for year in range(2010, 2014)]


# In[93]:


years


# In[94]:


years[0]


# In[95]:


years[0].join(years[1:])


# In[96]:


#create a function that returns the top names over a range of years

def top_names_range(sex, year_start, year_end):
    years = [top_names(sex, year) for year in range(year_start, year_end+1)]
    
    return years[0].join(years[1:])


# In[97]:


top_names_range('F', 1960, 1967)


# In[98]:


top_names_range('F', 1960, 1967).stack()


# In[99]:


#count the number of names for each name in the top years

top_names_range('F', 1960, 1967).stack().value_counts()


# In[107]:


#get the popular names for our latest data frame

popular_girls = top_names_range('F', 1960, 1967).stack().value_counts().index[:4]


# In[108]:


popular_girls


# In[109]:


popular_boys = top_names_range('M', 1960, 1967).stack().value_counts().index[:4]


# In[110]:


popular_boys


# In[111]:


#plot the popular boy names

pp.figure(figsize=(12,3))

for name in popular_boys:
    plot_name('M', name)
    
pp.legend(popular_boys)
pp.show()


# In[112]:


#plot the popular girl names

pp.figure(figsize=(12,3))

for name in popular_girls:
    plot_name('F', name)
    
pp.legend(popular_girls)
pp.show()


# In[ ]:




