#!/usr/bin/env python
# coding: utf-8

# In[1]:


#profiling and optimization are to help determine which parts of
#the code absorbe the most execution time and optimize them

#when to optimize?

#do we need optimization?
#if speed is not a problem, then there is no need to optimize;
#if yes: which parts of the code should be optimized?
#use a profiler such as cProfile in Python;
#usually most of the execution time occurs in a small part of the code
#optimize that code and leave the rest alone;
#if better performance is still needed, the code itself may have to be redesigned


# In[1]:


#1. this code is not optimized

def read_movies(src):
    with open(src) as fd:
        return fd.read().splitlines()

def is_duplicate(movie, movies):
    for m in movies:
        if m.lower() == movie.lower():
            return True
    return False

def find_duplicates_movies(src='movies.txt'):
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates

get_ipython().run_line_magic('time', 'find_duplicates_movies()')


# In[2]:


#write the profiler
#example from: https://docs.python.org/3/library/profile.html#profile.Profile

import cProfile, pstats, io

#profiler takes a function and that function can then be used
#as a decorator to another function;
#a decorater is a function that takes another function and adds some additional
#functionality to it

def profile(fnc):
    
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable() #start the profiler
        retval = fnc(*args, **kwargs) #apply it to the function
        pr.disable() #stop the profiler
        s = io.StringIO() #fetch the results of the profiler

        #print to screen
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval #return the value of the function
                      #in our case the list of movie duplicates
    
    return inner


# In[3]:


#2. let's see where the problem might be

def read_movies(src):
    with open(src) as fd:
        return fd.read().splitlines()

def is_duplicate(movie, movies):
    for m in movies:
        if m.lower() == movie.lower():
            return True
    return False

@profile
def find_duplicates_movies(src='movies.txt'):
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates

find_duplicates_movies()


# In[4]:


#3. if we want to optimize we need to
#look into is_duplicate() and in particular
#the string operation, lower();
#let's fix this by converting
#the string to lowercase when
#reading in the data

def read_movies(src):
    with open(src) as fd:
        return fd.read().splitlines()

def is_duplicate(movie, movies):
    for m in movies:
        #change the line below
        if m == movie:
            return True
    return False

@profile
def find_duplicates_movies(src='movies.txt'):
    movies = read_movies(src)
    
    #we have 10,000 movies so we write the code
    #below; call lower() 10,000 times instead
    #of 27 million times
    movies = [movie.lower() for movie in movies]
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates

find_duplicates_movies()


# In[5]:


#4. Can we improve this further?
#let's just check to see if the element
#is in the array; remove is_duplicate()
#entirely

def read_movies(src):
    with open(src) as fd:
        return fd.read().splitlines()

@profile
def find_duplicates_movies(src='movies.txt'):
    movies = read_movies(src)
    
    #we have 10,000 movies so we write the code
    #below; call lower() 10,000 times instead
    #of 27 million times
    movies = [movie.lower() for movie in movies]
    duplicates = []
    while movies:
        movie = movies.pop()
        if movie in movies:
            duplicates.append(movie)
    return duplicates

find_duplicates_movies()


# In[8]:


#zip function
#the zip() function returns a zip object, 
#which is an iterator of tuples where the 
#first item in each passed iterator is paired 
#together, and then the second item in each 
#passed iterator are paired together etc.

#if the passed iterators have different lengths, 
#the iterator with the least items decides the 
#length of the new iterator


a = ("Bugs", "Daffy", "Porky")
b = ("Daisy", "Minnie", "Babs", "Bianca")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x))


# In[6]:


#5. can we improve this further?
#we don't need is_duplicate() so
#that was removed but perhaps we
#can still improve the performance
#by changing our logic

#we are using an exponential solution
#we are looping thourgh our list of
#movies using the while loop and also
#inside the "if" statement to loop
#through the list;
#let's replace the while loop with a 
#list comprehension using sort()
#and turn the soltuion into a linear
#one

def read_movies(src):
    with open(src) as fd:
        return fd.read().splitlines()

@profile
def find_duplicates_movies(src='movies.txt'):
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    
    movies.sort() #identical movie titles are together now
    duplicates = [movie1 for movie1, movie2 in zip(movies[:-1], movies[1:])                   if movie1 == movie2]
    return duplicates

find_duplicates_movies()


# In[7]:


#even further improvement using sets

@profile
def find_duplicates_movies(src='movies.txt'):
    duplicates = set()
    movies = set()
    with open(src) as fd:
        for movie in fd.read().lower().splitlines():
            if movie in movies:
                duplicates.add(movie)
            else:
                movies.add(movie)
    return duplicates

find_duplicates_movies()


# In[12]:


#7. Even further

@profile
def find_duplicate_movies(src='movies.txt'):
   with open(src) as fd:
       lines = fd.read().lower().splitlines()

   duplicates = set(lines)
   return duplicates


# In[13]:


get_ipython().run_line_magic('time', 'find_duplicate_movies()')


# In[ ]:




