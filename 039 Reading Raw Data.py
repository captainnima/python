#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#setting the display options for pandas
pd.set_option('display.notebook_repr_html', True) #display pandas DataFrames as HTML tables
pd.set_option('display.precision', 2) #sets the precision for displaying numerical data to 2 decimal places
pd.set_option('display.float_format', '{:.2f}'.format) #sets the floating-point number format to two decimal 
                                                       #places using Python string formatting


# In[3]:


#load the data
m = pd.read_csv('military.csv', skiprows=4)


# In[4]:


m.head()


# In[5]:


#if reading a xls or xlsx file...
get_ipython().system('pip install xlrd')


# In[ ]:


#optional
#load the data, if excel
m = pd.read_excel('military.xls', skiprows=4)


# In[6]:


#print the names of the columns to check for any differences or mistakes.
print(m.columns)


# In[7]:


#finding the top 10 military spenders from 2017-2022

#sum the military spending across all years for each country
military_total = m.groupby('Country Name').sum()

#calculate the total military spending for each country from 2017 to 2022
military_total['Total'] = military_total.loc[:, '2017':'2022'].sum(axis=1)

#sort the countries based on their total military spending
top_ten_countries = military_total.nlargest(50, 'Total')['Total']

#print the top ten countries
print(top_ten_countries)


# In[8]:


#listing the top countries
top_countries = ['United States', 'China', 'India', 'Saudi Arabia', 'Russian Federation', \
                 'United Kingdom', 'Germany', 'France', 'Japan', 'Korea, Rep.']

#years 2017 to 2022
years = list(range(2017, 2023))
years


# In[9]:


#filter rows for the top countries
military = m[m['Country Name'].isin(top_countries)]

#filter columns for the specified years
military = military[['Country Name'] + [str(year) for year in years]]


military


# In[10]:


#option 1
#reindexing the DataFrames to match the top_countries_desc order
military = military.set_index('Country Name').loc[top_countries].reset_index()
military


# In[ ]:


#option 2
#resetting the index
military.reset_index(drop=True, inplace=True) #drop the old index, modifying the DataFrame in place
military


# In[11]:


military.head(10) # visualize the data


# In[12]:


#data shows the top 10 military spenders 

#create a table plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('off')  # Hide the axes
ax.table(cellText=military.head(10).values,
         colLabels=military.columns,
         cellLoc='center',
         loc='center')

#save the chart as a PNG file with high resolution (300 DPI)
plt.savefig('top_10_military.png', dpi=300, bbox_inches='tight', pad_inches=0.2) #increase the padding
plt.show()


# In[13]:


#creating graph showing the military spending of the top 10 countries

def plot_military_spending(military):
    #extracting unique country names from the 'Country Name' column
    countries = military['Country Name'].unique()

    #reordering countries to match the top_countries list
    countries = [country for country in top_countries if country in countries]

    #plotting the military spending for each country
    plt.figure(figsize=(12, 8))  # Set a larger figure size
    for country in countries:
        plt.plot(military.loc[military['Country Name'] == country, '2017':'2022'].values.flatten() / 1e9, label=country)

    #add title and labels to the plot
    plt.title('Military Spending of Countries (2017-2022)', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Military Spending (USD, Billions)', fontsize=14)
    
    #add a legend with country names
    plt.legend(title='Country', loc='upper left', fontsize=10, bbox_to_anchor=(1.02, 1), ncol=1)

    #set x-axis labels
    plt.xticks(ticks=range(6), labels=['2017', '2018', '2019', '2020', '2021', '2022'], fontsize=12)
    plt.yticks(fontsize=12)

    plt.grid(False)
    plt.margins(x=0)
    
    #save the chart as a PNG file with high resolution (300 DPI)
    plt.savefig('military_spending.png', dpi=300, bbox_inches='tight', pad_inches=0.2) #increase the padding
    plt.show() 


# In[14]:


plot_military_spending(military)


# In[ ]:









# In[ ]:




