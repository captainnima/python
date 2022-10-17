#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


print(dir(os))


# In[3]:


#print the current working directory

print(os.getcwd())


# In[4]:


#navigate

os.chdir('../')
print(os.getcwd())


# In[5]:


os.chdir('../../')
print(os.getcwd())


# In[6]:


os.chdir('Student/Desktop/Python')
print(os.getcwd())


# In[7]:


print(os.listdir())


# In[8]:


#create a folder
#2 methods: mkdir() makes a directory; makedirs() creates all 
#subdirectories also

os.mkdir('sample')


# In[14]:


os.makedirs('data/pubs/stuff/mystuff')


# In[10]:


#removing folders

os.rmdir('sample')


# In[11]:


os.rmdir('data')


# In[12]:


os.removedirs('data/pubs/stuff/mystuff')


# In[13]:


#shell utilities

import shutil


# In[15]:


shutil.rmtree('data')


# In[16]:


os.mkdir('sample')


# In[17]:


os.rename('sample', 'final')


# In[18]:


os.chdir('final')


# In[19]:


coffee = open('coffee.txt', 'w')
coffee.write('coffee time...followed by tea time')
coffee.close()


# In[20]:


os.rename('coffee.txt', 'tea.txt')


# In[21]:


#get some file info

os.stat('tea.txt')


# In[22]:


#picking a particular attribute

os.stat('tea.txt').st_size


# In[23]:


os.stat('tea.txt').st_mtime #modification time


# In[24]:


#making the time readable

from datetime import datetime


# In[25]:


print(datetime.fromtimestamp(os.stat('tea.txt').st_mtime))


# In[26]:


#traversing a directoring using walk()

print(os.getcwd())


# In[27]:


os.chdir('../../')
print(os.getcwd())


# In[28]:


os.walk(os.getcwd())


# In[30]:


#os.walk() returns a tuple of 3 values
#they are: dir path, directories, file names

os.chdir('Python')


# In[31]:


for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('current path: ', dirpath)
    print('directories: ', dirnames)
    print('files: ', filenames)
    print()


# In[32]:


#searching for a file using os.walk()
#then export

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for f in filenames:
        if f =='tea.txt':
            print('File name found')
            print(dirpath)
            f_out = open('/Users/Student/Desktop/tea_copy.txt', 'wb')
            f_in = open(dirpath + '/' + f, 'rb')
            data = f_in.read() #read all the data
            f_out.write(data)
            f_out.close()
            f_in.close()
            


# In[33]:


print(os.environ)


# In[34]:


print(os.environ.get('TEMP'))


# In[35]:


print(os.environ.get('STUFF'))


# In[36]:


print(os.environ.get('HOME'))


# In[37]:


print(os.environ.get('home'))


# In[38]:


#create a file path; this won't create the file iteself

file_path = os.path.join(os.environ.get('TEMP'), 'test.txt')


# In[39]:


print(file_path)


# In[40]:


#check to see if directory exists

os.path.exists('/tmp/data/test.txt')


# In[45]:


os.path.exists('C:\\Users\\Student\\AppData\\Local\\Temp')


# In[46]:


#checking to see if something is a file or directory

os.path.isdir('C:\\Users\\Student\\AppData\\Local\\Temp')


# In[49]:


os.path.isdir('C:\\Users\\Student\\Desktop\\Python\\final\tea.txt')


# In[50]:


#split a file and its extention

os.getcwd()


# In[51]:


os.path.splitext('final/tea.txt')


# In[ ]:




