#!/usr/bin/env python
# coding: utf-8

# # 034 CSV

# In[1]:


#working with csv files

import csv


# In[2]:


csv_file = open('sample.csv', 'r')
csv_reader = csv.reader(csv_file)


# In[3]:


print(csv_reader)


# In[4]:


#we need to iterate over the csv_reader

for line in csv_reader:
    print(line) #each line is a list of values
    print()


# In[5]:


#let's get all the emails

csv_file = open('sample.csv', 'r')
csv_reader = csv.reader(csv_file)
for line in csv_reader:
    print(line[4])


# In[6]:


#we don't want to see the header so let's step over it

csv_file = open('sample.csv', 'r')
csv_reader = csv.reader(csv_file)
next(csv_reader) #step over the item
for line in csv_reader:
    print(line[4])


# In[9]:


#writing to a csv file with '-' as delimiter

csv_file = open('sample.csv', 'r')
csv_reader = csv.reader(csv_file)

new_file = open('new_sample.csv', 'w')
csv_writer = csv.writer(new_file, delimiter='-')

for line in csv_reader:
    csv_writer.writerow(line)
    print('.', end='')
csv_file.close()


# In[11]:


#writing to a tab delimited file

csv_file = open('sample.csv', 'r')
csv_reader = csv.reader(csv_file)

tab_file = open('tab_sample.csv', 'w')
csv_writer = csv.writer(tab_file, delimiter='\t')

for line in csv_reader:
    csv_writer.writerow(line)
    print('.', end='')
csv_file.close()


# In[12]:


csv_file = open('tab_sample.csv', 'r')
csv_reader = csv.reader(csv_file, delimiter='\t')
for line in csv_reader:
    print(line)
csv_file.close()


# In[ ]:





# In[ ]:




