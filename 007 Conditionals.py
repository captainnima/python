#!/usr/bin/env python
# coding: utf-8

# In[1]:


#conditionals evaluate to True or False


# In[2]:


if True:
    print("it was true")


# In[3]:


if False:
    print("it was false")


# In[6]:


language = "Python"

if language == "Python":
    print(True)
else:
    print(False)


# In[7]:


if language == "Java":
    print('Java')
elif language == 'Python':
    print('Python')
else:
    print('Not sure')


# In[8]:


#there is not switch/case statements in Python


# In[9]:


#boolean operators
#and, or, not

user = 'admin'
logged_in = True

if user == 'admin' and logged_in == True:
    print('logged in')
else:
    print('bad credentials')


# In[10]:


user = 'admin'
logged_in = False

if user == 'admin' and logged_in == True:
    print('logged in')
else:
    print('bad credentials')


# In[11]:


user = 'admin'
logged_in = False

if user == 'admin' or logged_in == True:
    print('logged in')
else:
    print('bad credentials')


# In[12]:


user = 'admin'
logged_in = True

if user == 'admin' and not logged_in == False:
    print('logged in')
else:
    print('bad credentials')


# In[13]:


#object identity using the "is" keyword
#tests whether two objects have the same ID in memory

a = [1,2,3]
b = [1,2,3]


# In[14]:


a


# In[15]:


b


# In[16]:


a == b


# In[17]:


a is b


# In[18]:


print(id(a), id(b))


# In[19]:


b = a


# In[20]:


print(id(a), id(b))


# In[21]:


a is b


# In[22]:


print(a)
print(b)


# In[23]:


a.append(19)


# In[24]:


print(a)


# In[25]:


print(b)


# In[26]:


#what evaluates to True and what to False in Python

#everything that evaluates to False in Python
#1. False
#2. None
#3. zero of any numeric type
#4. any empty sequence or collection like '', "", (), []
#5. any empty mapping such as {}

#everything else is generally evaluate to True


# In[27]:


condition = False

if condition:
    print(True)
else:
    print(False)


# In[28]:


condition = None

if condition:
    print(True)
else:
    print(False)


# In[29]:


condition = 0

if condition:
    print(True)
else:
    print(False)


# In[30]:


condition = 0.0

if condition:
    print(True)
else:
    print(False)


# In[31]:


condition = ''

if condition:
    print(True)
else:
    print(False)


# In[32]:


condition = ()

if condition:
    print(True)
else:
    print(False)


# In[33]:


condition = []

if condition:
    print(True)
else:
    print(False)


# In[34]:


condition = {}

if condition:
    print(True)
else:
    print(False)


# In[35]:


condition = set()

if condition:
    print(True)
else:
    print(False)


# In[36]:


condition = True

if condition:
    print(True)
else:
    print(False)


# In[37]:


condition = 1

if condition:
    print(True)
else:
    print(False)


# In[38]:


condition = 'a'

if condition:
    print(True)
else:
    print(False)


# In[39]:


condition = (0,)

if condition:
    print(True)
else:
    print(False)


# In[40]:


condition = ['Math']

if condition:
    print(True)
else:
    print(False)


# In[42]:


condition = {0}

if condition:
    print(True)
else:
    print(False)


# In[43]:


condition = {1: 'Pebbles'}

if condition:
    print(True)
else:
    print(False)


# In[44]:


condition = [{}]

if condition:
    print(True)
else:
    print(False)


# In[ ]:




