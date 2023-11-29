#!/usr/bin/env python
# coding: utf-8

# # PY031 Generators

# In[ ]:


#why use generators and their advantage over lists


# In[1]:


#first a list

def square(nums):
    result = []
    for i in nums:
        result.append(i**2)
    return result

my_numbers = square([1,2,3,4,5])
print(my_numbers)


# In[2]:


#let's do this via a generator

def square(nums):
    for i in nums:
        yield i**2 #yield creates a generator


my_numbers = square([1,2,3,4,5])
print(my_numbers)


# In[ ]:


#the generator returns an object
#unlike a list, it does not compute and store
#the results in memory
#to get to the items, we can use the next()
#method or loop over it


# In[3]:


next(my_numbers)


# In[4]:


next(my_numbers)


# In[5]:


next(my_numbers)


# In[6]:


for num in my_numbers:
    print(num)


# In[7]:


#let's use a list comprehension

my_numbers = [i*i for i in [1,2,3,4,5]]
print(my_numbers)


# In[8]:


#to make it a generator, just use ()

my_numbers = (i*i for i in [1,2,3,4,5])
print(my_numbers)


# In[9]:


next(my_numbers)


# In[10]:


next(my_numbers)


# In[11]:


next(my_numbers)


# In[12]:


my_numbers = (i*i for i in [1,2,3,4,5])
print(my_numbers)


# In[13]:


#converting a generator to a list

print(list(my_numbers))


# In[ ]:


#because generators do not return the values immediately,
#they are not memory hungry and values are popped
#as they are needed

#let's compare


# In[14]:


get_ipython().system('pip install memory_profiler')


# In[15]:


import memory_profiler
import random
import time

names = ['Bugs', 'Daffy', 'Porky', 'Pete', 'Marvin', 'Pepe', 'Foghorn', 'Charlie']
majors = ['Computer Science', 'Math', 'Basket Weaving', 'Arts', 'Physics']

print('Memory (Before): {}'.format(memory_profiler.memory_usage()))
print()

def character_list(num_character):
    result = []
    for i in range(num_character):
        character = {
                        'id': i,
                        'name': random.choice(names),
                        'major': random.choice(majors)
                    }
        result.append(character)
        
    return result

def character_generator(num_character):
    for i in range(num_character):
        character = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield character

#for list

t1 = time.perf_counter()
character = character_list(1000000)
t2 = time.perf_counter()

print("List stats")
print('Memory (After): {}'.format(memory_profiler.memory_usage()))
print('Took {} seconds'.format(t2-t1))

print()
print("******************")
print()

#for generator
t1 = time.perf_counter()
character = character_generator(1_000_000)
t2 = time.perf_counter()

print("Generator stats")
print('Memory (After): {}'.format(memory_profiler.memory_usage()))
print('Took {} seconds'.format(t2-t1))


# In[16]:


next(character)


# In[17]:


next(character)


# In[18]:


next(character)


# In[ ]:




