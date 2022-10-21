#!/usr/bin/env python
# coding: utf-8

# In[9]:


#use the open() method to open and work with files

f = open('presidents.txt', 'w') #text: r, w, a, r+, a+; binary: rb, wb, ab


# In[36]:


p = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson', 'Van Buren', 'Polk']


# In[11]:


for president in p:
    print(president)


# In[12]:


for president in p:
    f.write(president)
f.close()


# In[13]:


f = open('presidents.txt', 'r+')

for president in p:
    f.write(president + '\n')
f.close()


# In[14]:


f = open('presidents.txt', 'r')

for president in f:
    print(president)


# In[16]:


f.close()
f = open('presidents.txt', 'r')
for president in f:
    print(president, end='')


# In[17]:


f.close()


# In[18]:


#another way to open a file which automatically closes it is using a 
#"with" context manager

with open('presidents.txt', 'r') as f:
    for p in f:
        print(p, end='')
    print()
print('The file is now closed')


# In[19]:


print(f.closed)


# In[20]:


print(f.mode)


# In[21]:


#readlines() returns a list of values

with open('presidents.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)


# In[22]:


f_contents[2]


# In[23]:


with open('presidents.txt', 'r') as f:
    f_contents = f.readlines()
    p_contents = []
    for p in f_contents:
        p = p.strip()
        p_contents.append(p)
    print(p_contents)


# In[24]:


with open('presidents.txt', 'r') as f:
    f_contents = f.readline() #readline() without the s reads the first line
    print(f_contents)


# In[25]:


with open('presidents.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)


# In[26]:


with open('presidents.txt', 'r') as f:
    f_contents = f.read(12)
    print(f_contents)


# In[27]:


#specifying a location to seek

with open('presidents.txt', 'r') as f:
    f.seek(12)
    f_contents = f.read(21)
    print(f_contents)


# In[28]:


#reading binary files

with open('disney.jpg', 'rb') as f:
    f.seek(11)
    f_contents = f.read(23)
    print(f_contents)


# In[29]:


#do a file copy

with open('disney.jpg', 'rb') as f:
    f_contents = f.read()
    
with open('mouse.jpg', 'wb') as o:
    o.write(f_contents)


# In[30]:


#what if we don't know how large the file is?

size_to_read = 10 #bytes

with open('presidents.txt', 'r') as f:
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)


# In[32]:


#viewing where we are

size_to_read = 10 #bytes

with open('presidents.txt', 'r') as f:
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(str(f.tell()))
        print(f_contents, end='')
        f_contents = f.read(size_to_read)


# In[33]:


#writing to files

with open('presidents.txt', 'r') as f:
    f.write('Lincoln')


# In[34]:


#this overwrites the file
with open('presidents.txt', 'w') as f:
    f.write('Lincoln')


# In[37]:


f = open('presidents.txt', 'r+')

for president in p:
    f.write(president + '\n')
f.close()


# In[38]:


#this one appends to the end
with open('presidents.txt', 'a') as f:
    f.write('Lincoln')


# In[ ]:




