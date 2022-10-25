#!/usr/bin/env python
# coding: utf-8

# In[1]:


#error handling (exception handling)


# In[2]:


try:
    x,y = 10,9
    print(x/y)
except:
    print('Error occurred')


# In[3]:


try:
    x,y = 10,0
    print(x/y)
except:
    print('Error occurred')


# In[4]:


try:
    x,y = 10,9
    print(x/y)
except:
    print('Error occurred')
else: #optional: this one executes if no error
    print('coffee time')


# In[5]:


try:
    x,y = 10,0
    print(x/y)
except:
    print('Error occurred')
else: #optional: this one executes if no error
    print('coffee time')


# In[6]:


try:
    x,y = 10,9
    print(x/y)
except:
    print('Error occurred')
else: #optional: this one executes if no error
    print('coffee time')
finally: #optional: this one runs no matter what
    print('afternoon tea time')


# In[7]:


try:
    x,y = 10,0
    print(x/y)
except:
    print('Error occurred')
else: #optional: this one executes if no error
    print('coffee time')
finally: #optional: this one runs no matter what
    print('afternoon tea time')


# In[ ]:




