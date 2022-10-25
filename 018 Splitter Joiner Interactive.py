#!/usr/bin/env python
# coding: utf-8

# In[1]:


#splitter joiner interactive


# In[2]:


import os
import os.path


# In[7]:


#splitter

def menu():
    print('Welcome to splitter')
    print()
    print('You will need to specify a file name and a split size')
    file_name = input('Enter a file name: ')
    buffersize = int(input('Enter the split size in bytes: '))
    return file_name, buffersize

def clean_up(file_name):
    try: #try to cleanup the leftovers
        meta_file = file_name + '.meta'
        in_file = open(meta_file, 'r')
        meta_info = in_file.readlines()
        splits = int(meta_info[2])
        for i in range(splits):
            os.remove(file_name + str(i))
        
    except:
        pass

def splitter():
    responses = menu()
    
    try:
        file_name = responses[0]
        if os.path.isfile(file_name): #if file name exists in the directory
            clean_up(file_name)
        else:
            pass
        
        buffersize = responses[1]
        in_file = open(file_name, 'rb')
        split_file_prefix = file_name
        buffer = in_file.read(buffersize)
        i = 0
        while len(buffer):
            split_file_prefix += str(i)
            out_file = open(split_file_prefix, 'wb')
            out_file.write(buffer)
            out_file.close()
            print('.', end='') #progressbar
            buffer = in_file.read(buffersize)
            i += 1
            split_file_prefix = file_name
        
        print()
        print('Split complete')
        
        #create a meta file
        out_file = open(file_name + '.meta', 'w')
        out_file.write(split_file_prefix + '\n')
        out_file.write(str(buffersize) + '\n')
        out_file.write(str(i))
        
        out_file.close()
        in_file.close()
        
    except:
        print('File not found or some other error')
    


# In[9]:


splitter()


# In[13]:


#joiner

def menu():
    print('Welcome to file joiner')
    print()
    print('You will need to specify the original file name')
    file_name = input('Enter the original file name: ')
    return file_name

def joiner():
    try:
        file_name = menu()
        meta_file = file_name + '.meta'
        
        in_file = open(meta_file, 'r')
        meta_info = in_file.readlines()
        split_file_prefix = meta_info[0].strip()
        buffersize = int(meta_info[1].strip())
        splits = int(meta_info[2])
        
        try:
            os.remove('New' + file_name)
        except:
            pass
        
        out_file = open('New' + file_name, 'ab')
        in_file = open(split_file_prefix + str(0), 'rb')
        buffer = in_file.read(buffersize)
        i = 0
        
        while len(buffer):
            out_file.write(buffer)
            print('.', end='')
            i += 1
            if i == splits:
                break
            split_file_prefix = meta_info[0].strip()
            split_file_prefix += str(i)
            in_file = open(split_file_prefix, 'rb')
            buffer = in_file.read(buffersize)
        
        in_file.close()
        out_file.close()
        print()
        print('Files rejoined. File name is: New' + file_name)
        
    except:
        print('Nonexistent file or some other error')


# In[14]:


joiner()


# In[ ]:




