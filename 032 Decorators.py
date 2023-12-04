#!/usr/bin/env python
# coding: utf-8

# # 032 Decorators

# In[1]:


#first class functions or higher order functions
#allow functions to be treated as values
#they can be passed as parameters


# In[ ]:


#algebra concepts
#f(x) = x+7 --> y=f(x)
#g(x) = x-10 --> y = f(g(x))


# In[4]:


def outer_function():
    message = "hi there"
    
    def inner_function():
        print(message)
    return inner_function() #execute the function and return the result

outer_function


# In[ ]:


#A decorator is just a function that takes 
#another function as an argument, 
#adds some kind of functionality, 
#and then returns another function


# In[9]:


def outer_function():
    message = "hi there"
    
    def inner_function():
        print(message)
    return inner_function #do not execute the function
                          #return the inner_function 
                          #waiting to be executed

outer_function()


# In[10]:


my_func = outer_function()


# In[11]:


my_func


# In[12]:


my_func()


# In[ ]:


#notice the () executed the function
#this is closure


# In[14]:


outer_function()()


# In[15]:


def outer_function(message):
   
    def inner_function():
        print(message)
    return inner_function #do not execute the function

tea_func = outer_function('tea time')
coffee_func = outer_function('coffee time')

#each of the functions above are assigned to the
#inner function, ready to be executed


# In[19]:


tea_func()


# In[17]:


coffee_func()


# In[20]:


#now decorator

def decorator_function(message):
    def wrapper_function():
        print(message)
    return wrapper_function #returns the wrapper function
                            #ready to be executed


# In[22]:


decorator_function('Coffee time')() #add ()


# In[23]:


#let's instead of printing a message, pass in a function
#and execute the function
#this makes the construct a decorator

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function #returns the wrapper function
                            #ready to be executed


# In[24]:


def display():
    print('display function ran')


# In[25]:


display()


# In[26]:


decorated_display = decorator_function(display)


# In[27]:


decorated_display() #execute the wrapper_function


# In[28]:


#without changing the functionality of the display()
#function, we can make changes to the wrapper

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function #returns the wrapper function
                            #ready to be executed


# In[31]:


@decorator_function
def display():
    print('display function ran')


# In[32]:


display()


# In[ ]:


#@decorator_function is the same as writing
#decorated_display = decorator_function(display)


# In[33]:


#what about arguments?

def display_info(name, age):
    print('display ({}, {})'.format(name, age))


# In[34]:


display_info('Bugs', '47')


# In[35]:


@decorator_function
def display_info(name, age):
    print('display ({}, {})'.format(name, age))


# In[36]:


display_info('Bugs', '47')


# In[39]:


#we need to modify our wrapper function

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
                            #execute this function and return its result
    return wrapper_function
                            #returns the wrapper function
                            #ready to be executed
#note: *args must come before **kwargs;
#*args is a list of positional arguments
#**kwargs is a list of key/value pair arguments
#both are optional and the naming doesn't matter


# In[40]:


@decorator_function
def display():
    print('display function ran')


# In[41]:


@decorator_function
def display_info(name, age):
    print('display ({}, {})'.format(name, age))


# In[42]:


display()


# In[43]:


display_info('Bugs', '47')


# In[44]:


#using classes as decorators

class decorator_class(object): #inherit from object; not necessary
    def __init__(self, original_function):
        self.original_function = original_function
        
    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


# In[45]:


@decorator_class
def display():
    print('display function ran')


# In[46]:


display()


# In[47]:


@decorator_class
def display_info(name, age):
    print('display ({}, {})'.format(name, age))


# In[48]:


display_info('Bugs', '47')


# In[49]:


#let's create a decorator to keep track of logging

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.txt'.format(orig_func.__name__), level=logging.INFO)
    
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper #ready to be executed


# In[50]:


@my_logger
def display_info(name, age):
    print('display ({}, {})'.format(name, age))
    
#a file named after the calling function, display_info.txt
#is created but is empty currently


# In[51]:


display_info('Bugs', '47')


# In[52]:


display_info('Bugs', '47', id=201)


# In[ ]:


#ignore the error and check the file display_info.txt


# In[53]:


#creating a decorator that takes an argument
#first a regular decorator

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        result = original_function(*args, **kwargs)
        print('executed after', original_function.__name__, '\n')
        return result #execute this function and return its result
    return wrapper_function


# In[54]:


@decorator_function
def display_info(name, age):
    print('display ({}, {})'.format(name, age))


# In[55]:


display_info('Bugs', '47')


# In[59]:


#let's say we want a customizable prefix for all the print statements

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'wrapper executed this before {}'.format(original_function.__name__))
            result = original_function(*args, **kwargs)
            print(prefix, 'executed after', original_function.__name__, '\n')
            return result #execute this function and return its result
        return wrapper_function
    return decorator_function #add this


# In[60]:


@prefix_decorator('coffee time...')
def display_info(name, age):
    print('display ({}, {})'.format(name, age))


# In[61]:


display_info('Bugs', '47')


# In[ ]:




