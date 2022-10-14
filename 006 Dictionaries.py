#!/usr/bin/env python
# coding: utf-8

# In[1]:


#empty dicts

dict_1 = {}
dict_2 = dict()


# In[2]:


student = {'name': 'Bugs Bunny', 'age': 52, 'courses': ['Math', 'Physics']}
student


# In[3]:


type(student)


# In[4]:


student['name']


# In[5]:


print(student['name'])


# In[6]:


student['age']


# In[7]:


student['courses']


# In[8]:


student['courses'][1]


# In[9]:


student['phone']


# In[10]:


student.get('name')


# In[11]:


student.get('phone')


# In[12]:


student.get('courses')


# In[13]:


print(student.get('phone'))


# In[14]:


#using a default value as a second parameter
print(student.get('phone', 'Not Found'))


# In[16]:


student.update({'name': 'Daffy Duck', 'age': 57, 'phone': '703-555-1212'})


# In[17]:


student


# In[18]:


student.get('phone')


# In[19]:


dict_1 = {name: 'Bugs'}


# In[20]:


dict_1 = {1: 'Bugs'}


# In[21]:


dict_1


# In[22]:


#to delete

del student['age']
student


# In[23]:


li = ['test', 'sample']


# In[24]:


li


# In[25]:


del li[0]


# In[26]:


li


# In[27]:


#using pop() method to return the value; pop() removes the value from dict


# In[28]:


name = student.pop('name')


# In[29]:


name


# In[30]:


student


# In[31]:


print(len(student))


# In[32]:


#view the keys
print(student.keys())


# In[33]:


#view the values
print(student.values())


# In[34]:


#view both keys and values
print(student.items())


# In[35]:


#looping through a dict

for k in student: #this way it only gets the keys
    print(k)


# In[36]:


for key, value in student.items():
    print(key, value)


# In[37]:


#just the values
for v in student.values():
    print(v)


# In[38]:


import this


# In[ ]:




