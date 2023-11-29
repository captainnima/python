#!/usr/bin/env python
# coding: utf-8

# # 030 Iterators

# In[ ]:


#iterators and iterables are two different things
#a list is iterable but is not an iterator
#let's see the meanings


# In[1]:


#what does it mean when something is iterable?
#it means it can be looped over for one thing

nums = [1,2,3]

for num in nums:
    print(num)


# In[2]:


#how can we tell if something is iterable?
#it needs to have __iter__() method
#let's see if list has this method

print(dir(nums))


# In[ ]:


#__iter__() is there so it is iterable


# In[ ]:


#what is an iterator?
#it is an object with a state that knows where it is during
#an iteration
#iterators also know how to get their next value with the
#__next__() method; as can be seen a list does not have __next__()
#so a list is not an iterator


# In[3]:


print(next(nums))


# In[4]:


nums = [1,2,3]

i_nums = nums.__iter__()

print(i_nums)
print(dir(i_nums))


# In[5]:


#we can also write it this way
#using a background method that calls
#__iter__()

nums = [1,2,3]

i_nums = iter(nums)

print(i_nums)
print(dir(i_nums))


# In[6]:


#we got a list iterator and notice __next__() is there

print(next(i_nums))


# In[7]:


#i_nums is an iterator that was created from a list
#remember an iterator is an object with a state so
#it will remember its position
#iterators can only go forward

print(next(i_nums))
print(i_nums.__next__())


# In[8]:


print(next(i_nums))


# In[9]:


#making our own iterator
#this class behaves like the built-in range() function

class MyRange:
    def __init__(self, start, end): #start and end points
        self.value = start
        self.end = end
        
    def __iter__(self):
        return self #since it is returing the object
                    #the __next__() is also returned
                    #(below) so it is an iterator
    
    def __next__(self):
        if self.value >= self.end: #use > to be inclusive
            raise StopIteration
            
        current = self.value
        self.value += 1
        return current
            


# In[10]:


nums = MyRange(1,10)

for num in nums:
    print(num)


# In[11]:


#as can be seen, this object is iterable but
#it is also an iterator since it has __next__()


# In[12]:


nums = MyRange(1,10)

print(next(nums))


# In[13]:


print(next(nums))


# In[ ]:


#keep in mind that generators yield a value instead of returing
#a result
#generators are iterators


# In[14]:


#let's create a generator function that
#returns an iterator that is also iterable

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


# In[15]:


print(type(my_range))


# In[16]:


nums = my_range(1,10)

print(next(nums))


# In[18]:


print(next(nums))


# In[19]:


for i in nums:
    print(i)


# In[ ]:


#iterators are useful for writing memory efficient programs
#for instance if writing a password cracker using a list
#of passwords; we can use an iterator to use one password
#at a time without loading all the passwords in the memory


# In[ ]:




