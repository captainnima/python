#!/usr/bin/env python
# coding: utf-8

# In[1]:


#collections are also called sequences
#we will look at lists, tuples, and sets


# In[2]:


#lists; created using the []

courses = [] #empty list


# In[3]:


courses


# In[4]:


courses = ['History', 'Math', 'Physics', 'Coding', 3]


# In[5]:


courses


# In[6]:


print(len(courses))


# In[7]:


courses[1:3]


# In[8]:


courses.remove(3)
courses


# In[9]:


courses.append('Art')
courses


# In[10]:


more_courses = ['English', 'Drafting']
more_courses


# In[11]:


courses.extend(more_courses)
courses


# In[12]:


courses.insert(2, 'Chemistry')
courses


# In[13]:


#pop() returns a value

phy = courses.pop(3)
phy


# In[14]:


courses


# In[15]:


for item in courses:
    print(item)


# In[16]:


message = "It's coffee time"
for m in message:
    print(m)


# In[17]:


#using the "in" operator

print('Math' in courses)


# In[18]:


courses


# In[19]:


'Programming' in courses


# In[20]:


#to get the index, use the enumerate() function
#returns the index and the value

for i, c in enumerate(courses):
    print(i, '-->', c)


# In[21]:


#we can choose the index ourselves

for i, c in enumerate(courses, start=1):
    print(i, '-->', c)


# In[22]:


#using the join() method with strings

courses_str = ';'.join(courses)
print(courses_str)


# In[23]:


courses


# In[24]:


#split() method; creates a list from a string

courses_str


# In[25]:


new_list = courses_str.split(';') #no param means split over space
new_list


# In[27]:


#tuples; immutable
#use the comma to create

schools = ('GMU', 'GWU')
print(type(schools))


# In[28]:


#() are not necessary

schools = 'Stanford', 'MIT', 'GWU'
print(type(schools))


# In[29]:


t = (9)
print(type(t))


# In[30]:


m = (9,)
print(type(m))


# In[31]:


#empty tuple
e = tuple()
print(type(e))


# In[32]:


schools


# In[33]:


schools[1:2]


# In[34]:


schools.append('GMU')


# In[35]:


#sets
#values are unordered and no duplicates are kept;
#duplicates are removed; use {} to create
set_courses = {'Coding', 'Math', 'Physics', 'Coding'}
set_courses


# In[36]:


print('Math' in set_courses)


# In[37]:


art_courses = {'Art', 'Drafting', 'Coding'}
art_courses


# In[38]:


set_courses.intersection(art_courses)


# In[39]:


set_courses.difference(art_courses)


# In[40]:


set_courses.union(art_courses)


# In[41]:


#creating empty list, tuple, set

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} #doesn't work
empty_set = set()


# In[42]:


my_set = {}
print(type(my_set))


# In[ ]:




