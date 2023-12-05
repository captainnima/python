#!/usr/bin/env python
# coding: utf-8

# # 037 Climate Change

# In[4]:


#Global Temps

import math
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import chart_studio.plotly as py


# In[1]:


get_ipython().system('pip install plotly')


# In[2]:


get_ipython().system('pip install chart_studio')


# In[ ]:


#py.sign_in('*********','***************') #optional usually


# In[5]:


plotly.offline.init_notebook_mode()


# In[6]:


#import the data; data comes from NOAA

global_temp = pd.read_csv('Global_temp.csv', index_col=0, header=0)
global_gas = pd.read_excel('Global_Greenhouse_Gas.xls', 
                           index_col=0, header=3).fillna(0)


# In[7]:


global_temp.head()


# In[8]:


global_gas.head()


# In[9]:


cols=[]
for i in range(1970,2012+1):
    cols.append(str(i))
cols


# In[10]:


global_gas = global_gas[cols[:len(cols)]]
global_gas.head()


# In[13]:


state_gas = pd.read_excel('State_Carbon_dioxide.xlsx', header=4)
state_gas = state_gas.drop(['percent', 'absolute'], axis=1).dropna()


# In[14]:


state_gas.head()


# In[15]:


global_gas['1972']


# In[16]:


df = global_gas['1970']
df


# In[17]:


top = df.sort_values(ascending=False)
top


# In[18]:


top = top.reset_index().head(10)
top


# In[19]:


top.index = top.index + 1
top


# In[20]:


#for a given year, let's determine the top 10 emitters

def topten(year, total=10):
    df = global_gas[year]
    top = df.sort_values(ascending=False)
    top = top.reset_index().head(total)
    top.index = top.index + 1
    return top


# In[21]:


topten('1970')


# In[22]:


topten('2010')


# In[23]:


df = global_gas['1970']
top = df.sort_values(ascending=False)
top


# In[24]:


top = top.reset_index()
top.index = top.index + 1
top


# In[27]:


top[10:].sum()[1]


# In[28]:


#for a given year make a pie chart of the top 10 emitters

def PiePlot(year):
    df = global_gas[year]
    top = df.sort_values(ascending=False)
    top = top.reset_index()
    top.index = top.index + 1
    others = top[10:].sum()[1]
    top = top[:10]
    top.loc[11] = ['All Other Countries', others]
    
    countryPlot = top[year].plot.pie(subplots=True,
                                     autopct='%0.1f',
                                     fontsize=10,
                                     figsize=(10,10),
                                     legend=False,
                                     labels=top['Country Name'],
                                     shadow=False,
                                     explode=(0.15,0,0,0,0,0,0,0,0,0,0),
                                     startangle=90)


# In[29]:


PiePlot('2010')
plt.show()


# In[30]:


PiePlot('1970')
plt.show()


# In[31]:


global_temp.head()


# In[32]:


#show the global temps over time

ax = global_temp['Value'].plot()
ax.set_xlabel('Year')
ax.set_ylabel('Global Temps 5 Year Mean (F)')
plt.show()


# In[33]:


#lets look at emissions over time
ax = global_gas.sum().plot()
ax.set_xlabel('Year')
ax.set_ylabel('Total Greenhouse Emissions (kt of Co2 equiv.)')
plt.show()


# In[34]:


#calculate the correlation coefficient between the two

x = global_gas.sum()
y = global_temp.reset_index()['Value']

top = 0
b1 = 0
b2 = 0
for i in range(len(x)):
    top = (x[i]-x.mean()) * (y[i]-y.mean()) + top
    b1 = (x[i]-x.mean())**2 + b1
    b2 = (y[i]-y.mean())**2 + b2
    
r = top/(math.sqrt(b1)*math.sqrt(b2))
r


# In[35]:


import plotly.graph_objects as go


# In[44]:


#for a given year, let's map US's contribution 
#to greenhouse by state using plotly

scale = [[0.0, 'rgb(223,221,228)'], 
         [0.2, 'rgb(199,199,201)'],
         [0.4, 'rgb(169,170,201)'], 
         [0.6, 'rgb(139,135,181)'],
         [0.8, 'rgb(98,88,158)'], 
         [1.0, 'rgb(63,20,122)']]


def mapper(year):     
    fig = go.Figure(data=go.Choropleth(
        locations = state_gas['State'],
        z = state_gas[int(year)],
        text=state_gas['State'],
        locationmode='USA-states',
        colorscale=scale,
        autocolorscale=False,
        reversescale=False,
        marker_line_color='rgb(255,255,255)',
        marker_line_width=2,
        colorbar_tickprefix = '',
        colorbar_title = 'Million Metric Tons CO2 In ' + str(year)
    ))

    fig.update_layout(
        title_text = 'State Energy-related CO2 Emissions In ' + 
                     str(year) + '<br>Hover for value',
        geo=dict(
            showframe=False,
            showcoastlines=True,
            showlakes=True,
            lakecolor='rgb(95,145,237)',
            projection_type='albers usa') #try equirectangular
        
        ,annotations = [dict(
            x=0.7, #from left between 0-1
            y=0.05, #from bottom between 0-1
            xref='paper',
            yref='paper',
            text='Source: <a href="https://www.noaa.gov/">NOAA</a>',
            showarrow = False
        )]
    )
    fig.show()


# In[45]:


mapper(2005)


# In[ ]:


#old plotly code

'''    data = [dict(type='choropleth',
                 colorscale=scale,
                 locations=state_gas['State'],
                 z=state_gas[year],
                 locationmode='USA-states',
                 text=state_gas['State'],
                 hoverinfo='location+z',
                 marker=dict(line=dict(color='rgb(255,255,255)', width=2)),
                 colorbar=dict(title='Million Metric Tons CO2 In ' + str(year)))]
    
    layout = dict(title='State Energy-related CO2 Emissions In ' + 
                  str(year) + '<br> Hover for value',
                  geo=dict(scope='USA',
                  projection=dict(type='albers usa'), 
                  showlakes=True, lakecolor='rgb(95,145,237)'))
    
    fig = go.Figure(dict(data=data, layout=layout)
    return py.iplot(fig, validate=False, filename='geomap-states-may-2020')'''


# In[ ]:




