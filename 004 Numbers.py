#!/usr/bin/env python
# coding: utf-8

# In[1]:


#working with numbers in Python


# In[2]:


num = 3
dec = 3.14


# In[3]:


print(num, type(num))
print(dec, type(dec))


# In[4]:


#operations

print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3//2) #floor operation; drops the decimal
print(3%2)
print(3**2)


# In[5]:


#use () to control the order of operations

print(3*2+4*7)


# In[6]:


print(3*(2+4)*7)


# In[7]:


#variable incrementing

num = 1
num += 2


# In[8]:


num


# In[9]:


num *= 4
num


# In[10]:


num /= 6
num


# In[11]:


print(abs(-3))


# In[12]:


print(round(3.78))


# In[13]:


print(round(3.78928282, 2))


# In[14]:


#comparisons

3 = 2 #assignment


# In[15]:


3 == 2


# In[16]:


3 == 3


# In[17]:


3 <= 2


# In[18]:


3 >= 2


# In[19]:


3 > 2


# In[20]:


3 < 2


# In[21]:


3 != 2


# In[22]:


num_1 = '100'
num_2 = '200'

print(num_1+ num_2)


# In[23]:


print(int(num_1) + int(num_2))


# In[24]:


num = -19

print(dir(num))


# In[25]:


abs(num)


# In[26]:


num.__abs__()


# In[28]:


#+ shorthand for __add__


# In[33]:


num + 3


# In[34]:


num.__add__(3)


# In[ ]:




