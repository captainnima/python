#!/usr/bin/env python
# coding: utf-8

# In[1]:


#splitter joiner


# In[5]:


def splitter():
    buffer_size = 1000000 #bytes
    in_file = open('Wildlife.wmv', 'rb')
    file_prefix = 'Wildlife'
    buffer = in_file.read(buffer_size)
    i = 0
    while len(buffer):
        file_prefix += str(i) #file_prefix = file_prefix + str(i)
        out_file = open(file_prefix, 'wb')
        out_file.write(buffer)
        out_file.close()
        print('.', end='') #progressbar
        buffer = in_file.read(buffer_size)
        i += 1
        file_prefix = 'Wildlife'
    in_file.close()
    print()
    print('Files splitted')


# In[6]:


splitter()


# In[12]:


def joiner():
    out_file = open('NewWildlife.wmv', 'ab')
    file_prefix = 'Wildlife'
    in_file = open(file_prefix + str(0), 'rb')
    buffer = in_file.read()
    i = 0
    while len(buffer):
        out_file.write(buffer)
        print('.', end='')
        i += 1
        if i == 27:
            break
        file_prefix = 'Wildlife'
        file_prefix += str(i)
        in_file = open(file_prefix, 'rb')
        buffer = in_file.read()
    out_file.close()
    print()
    print('Files rejoined')


# In[13]:


joiner()


# In[ ]:




