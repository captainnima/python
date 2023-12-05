#!/usr/bin/env python
# coding: utf-8

# # 036 XML

# In[1]:


import xml, os
from xml.etree import ElementTree


# In[2]:


full_file = 'reed.xml'


# In[3]:


dom = ElementTree.parse(full_file)


# In[4]:


dom


# In[5]:


courses = dom.findall('course/title')


# In[6]:


courses


# In[7]:


for c in courses:
    print(c.text)


# In[8]:


courses = dom.findall('course') #<course> tag


# In[9]:


courses


# In[10]:


for c in courses:
    title = c.find('title').text
    num = c.find('crse').text
    days = c.find('days').text
    instructor = c.find('instructor').text
    units = c.find('units').text
    
    print(' * {} [{}] {} - {} {}'.format(num, days, title, instructor, units))


# In[ ]:




