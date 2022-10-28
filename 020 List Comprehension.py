#!/usr/bin/env python
# coding: utf-8

# In[1]:


#create a list of cubes

cubes = []

for i in range(10):
    cubes.append(i**3)
    
print(cubes)


# In[2]:


#comprehension format -- [items of the list - loops to create those items - conditionals (optional)]

cubes = [i**3 for i in range(10)]
print(cubes)


# In[3]:


cubes_mod_5 = [i**3 for i in range(10) if i**3 % 5 == 0]
print(cubes_mod_5)


# In[ ]:




