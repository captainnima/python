#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Coffee time")
print('Tea time')


# In[2]:


print("Coffee time")
 print('Tea time')


# In[3]:


print("Coffee time")
print('Tea time')


# In[4]:


message = 'Coffee time'
print(message)


# In[5]:


message


# In[6]:


message = 'It\'s coffee time'
print(message)


# In[7]:


print(Message)


# In[8]:


print(type(message))


# In[9]:


message[3]


# In[10]:


message


# In[11]:


message[5]


# In[12]:


message[5:10]


# In[13]:


message[5:11]


# In[14]:


message[-1]


# In[15]:


message[-1:-5]


# In[16]:


message[-4:-1]


# In[17]:


message[-4:0]


# In[18]:


message[-4:]


# In[19]:


#a little trick
print(dir(message))


# In[20]:


message.title()


# In[21]:


message.upper()


# In[22]:


print(help(message))


# In[23]:


print(help(str))


# In[24]:


print(help(str.lower)) #more specific help


# In[25]:


message.lower()


# In[26]:


msg1 = 'coffee time'
msg2 = 'tea time'

print(msg1, msg2)


# In[27]:


print(msg1 + msg2)


# In[28]:


print('{} and {}'.format(msg1, msg2))


# In[29]:


print('{} and {}'.format(msg2, msg1))


# In[30]:


print('{} and {} and {} and {}'.format(msg1, msg2, msg2, msg1+msg2))


# In[31]:


print('{1} and {0}'.format(msg1, msg2))


# In[32]:


print(message)


# In[33]:


print(message.count('t'))


# In[34]:


print(message.find('coffee'))


# In[35]:


print(message.find('latte'))


# In[36]:


print(message.replace('e', 'z'))


# In[37]:


message


# In[39]:


message = message.replace('coffee', 'tea')


# In[40]:


message


# In[41]:


#F strings

message = f'{"coffee"}, {"tea"}'


# In[42]:


message


# In[43]:


d1, d2 = 'coffee', 'tea'
message = f'{d1}, {d2}'
print(message)


# In[44]:


#we can code directly in place inside the placeholder

message = f'{"coffee".upper()}, {"tea".upper()}'
print(message)


# In[ ]:




