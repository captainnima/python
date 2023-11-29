#!/usr/bin/env python
# coding: utf-8

# # 029 Context Managers

# In[ ]:


#context managers allow us to properly use resources in Python
#as to what we want to setup and tear down


# In[1]:


#let's see context manager for files
#first without a context manager

f = open('coffee.txt', 'w')
f.write('Coffee Time')
f.close()


# In[2]:


#using a context manager

with open('tea.txt', 'w') as f:
    f.write("Tea Time")


# In[ ]:


#with context manager we don't have to remember to close the file
#in this instance


# In[3]:


#creating the file context manager using classes

class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file #this matches the "f"
    
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()
        
        #the extra parameters are there for if we throw
        #an exception; they are needed for __exit__ dunder
        #method though we are not using them


# In[4]:


with Open_File('coffee.txt', 'w') as f:
    f.write("It's Coffee Time using classes")


# In[5]:


print(f.closed)


# In[6]:


#creating the file context manager using functions

from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f #the code within the with statement is going to run
                #this is the variable that comes after "as"
                #yield returns a generator function
    finally:
        f.close()
        print("Bye")


# In[7]:


with open_file("coffee.txt", 'w') as f:
    f.write("Coffee time using functions")


# In[8]:


#a practical example
#first without a context manager

import os

cwd = os.getcwd()
os.chdir('stuff1') #create this directory and add some files
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('stuff2') #create this directory and add some files
print(os.listdir())
os.chdir(cwd)


# In[9]:


#let's make this operation into a context manager

from contextlib import contextmanager

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


# In[12]:


with change_dir('stuff1'): #since yield didn't return anything
                           #as var is not needed
    print(os.listdir())


# In[ ]:




