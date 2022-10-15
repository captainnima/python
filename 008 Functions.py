#!/usr/bin/env python
# coding: utf-8

# In[1]:


#functions allow for modular code and code reuse


# In[2]:


def coffee_func():
    print('coffee time')


# In[3]:


coffee_func()


# In[4]:


def coffee_func():
    return 'coffee time'


# In[5]:


coffee_func()


# In[6]:


print(coffee_func())


# In[7]:


message = coffee_func()
message


# In[8]:


def tea_func():
    return 'tea time', 'afternoon'


# In[9]:


tea_func()


# In[10]:


tea_func()[0]


# In[11]:


tea_func()[1]


# In[12]:


message = tea_func()


# In[13]:


message[1]


# In[14]:


#pass keyword; means do nothing

def do_nothing():
    pass


# In[15]:


do_nothing()


# In[16]:


print(do_nothing())


# In[18]:


#daisy chain functions

print(coffee_func().upper())


# In[19]:


#working with arguments

def coffee_func(person):
    return 'coffee time for {}'.format(person)


# In[20]:


coffee_func('Bugs Bunny')


# In[21]:


coffee_func()


# In[22]:


def coffee_func(person = 'Bugs Bunny'):
    return 'coffee time for {}'.format(person)


# In[23]:


coffee_func()


# In[24]:


coffee_func('Porky Pig')


# In[25]:


#variable length list of arguments

def coffee_func(*args, **kwargs): #* is positional args and ** keywords args
    print(args)
    print(kwargs)


# In[26]:


coffee_func()


# In[27]:


coffee_func('Bugs', 'Daffy', 'Porky')


# In[28]:


coffee_func('Bugs', 'Daffy', 'Porky', name='Pete Puma', age=54)


# In[29]:


#first three are positional arguments; last two are keyword arguments
#positional arguments come as tuples
#keyword arguments are treated as dictionaries


# In[30]:


def tea_func(*args):
    print(args)


# In[31]:


tea_func('Bugs', 'Daffy', 'Porky')


# In[32]:


def hotcocoa_func(person='Bugs', **kwargs):
    print(kwargs)


# In[33]:


hotcocoa_func(name='Pete', last='Puma', age=54)


# In[35]:


courses = ['Math', 'Art', 'Coding']
info ={'name': 'Bugs Bunny', 'age': 55}

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# In[36]:


student_info(courses, info) #this doesn't work


# In[37]:


#* and ** operators unpack the list and the dict and pass the parameters

student_info(*courses, **info)


# In[ ]:




