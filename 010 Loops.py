#!/usr/bin/env python
# coding: utf-8

# In[1]:


#for loops
#loops over collections


# In[2]:


courses = ['History', 'Math', 'Art', 'Music', 'Physics', 'English']


# In[3]:


for c in courses:
    print(c)


# In[6]:


for i in range(2,7):
    print(i, i**2)


# In[7]:


for i in range(2, 30, 3):
    print(i)


# In[9]:


message = 'It is now coffee time'
for m in message:
    print (m)


# In[12]:


#while loops

c = 10

while c > 0:
    print(c**2)
    c -= 1


# In[14]:


#looking at "break" and "continue" keywords

for i in range(10):
    if i == 7:
        break #stop the loop completely
    print(i**2)


# In[15]:


for i in range(10):
    if i == 7:
        continue #stop the loop for this iteration
    print(i**2)


# In[ ]:




