#!/usr/bin/env python
# coding: utf-8

# # 033 First Class Functions

# In[1]:


#also known as higher order functions

#a programming language is said to have first-class
#functions if it treats functions as first-class
#citizens. This means the functions can be treated as
#values, be passed around as parameters, and be returned
#from other functions


# In[2]:


#f(x) = x+7 --> y = f(x): f(10) = 10+7 = 17 and y(7) = f(x) = f(10) = 17
#g(x) = x-10 --> z = g(x), y = f(g(x)) or y = f(z)


# In[3]:


def square(x):
    return x*x

y = square(5)


# In[4]:


print(square)


# In[5]:


print(y)


# In[7]:


square(5)


# In[8]:


#now do this

f = square


# In[9]:


print(square)


# In[10]:


print(f)


# In[11]:


print(f(5))


# In[12]:


#so f is now a function; the () execute the function


# In[13]:


#passing a function as an argument

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5])


# In[14]:


print(squares)


# In[15]:


def cube(x):
    return x*x*x


# In[16]:


cubes = my_map(cube, [1,2,3,4,5])


# In[17]:


print(cubes)


# In[18]:


#returning a function as a variable

def logger(msg):
    def log_message():
        print('log:', msg)
    return log_message


# In[20]:


log_hi = logger('hi there') #a function is returned and assigned to log_hi
log_hi() #execute the function


# In[21]:


log_hi


# In[22]:


def html_tag(tag):
    def wrap_text(text):
        print('<{0}>{1}</{0}>'.format(tag, text))
    
    return wrap_text


# In[23]:


print_h1 = html_tag('h1') #create the function
print_h1('Text Headline') #run the function


# In[24]:


print_h1('Coffee Time')


# In[27]:


#closure

def outer_function():
    message = "hi there"
    
    def inner_function():
        print(message)
    return inner_function() #execute the inner function and return it

outer_function() #execute the outer function


# In[28]:


#let's do this

def outer_function():
    message = "hi there"
    
    def inner_function():
        print(message)
    return inner_function # do not execute the inner function

my_func = outer_function


# In[29]:


my_func


# In[30]:


my_func()


# In[31]:


my_func()()


# In[32]:


my_func.__name__


# In[33]:


my_func().__name__


# In[ ]:


my_func = outer_function() #add the ()


# In[36]:


my_func()()


# In[ ]:


#a closure is an inner function that remembers and has access to
#variables in the local scope in which it was created even after
#the outer function has been done executing


# In[37]:


def outer_function(message): #add parameter
    
    def inner_function():
        print(message)
    return inner_function # do not execute the inner function

tea_func = outer_function('tea time')
coffee_func = outer_function('coffee time')


# In[39]:


tea_func()


# In[42]:


coffee_func()


# In[ ]:


#each function remembers the value of its own message variable


# In[ ]:




