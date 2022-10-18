#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pillow')


# In[1]:


from PIL import Image
import os


# In[2]:


print(os.getcwd())


# In[3]:


os.chdir('013 images')


# In[4]:


print(os.getcwd())


# In[5]:


print(os.listdir())


# In[8]:


#open and view an image

my_image = Image.open('2022-10-11 IMG_0154.jpg')


# In[9]:


my_image.show()


# In[10]:


#save a jpg as a png

my_image.save('2022-10-11 IMG_0154.png')


# In[12]:


#loop through the directory and save the jpgs as pngs

for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.jpeg'):
        print(f)
        i = Image.open(f)
        f_name, f_ext = os.path.splitext(f)
        i.save('{}.png'.format(f_name))


# In[13]:


print(os.listdir())


# In[15]:


#photo resizing

size_400 = (400, 400) #tuple

for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.jpeg'):
        print(f)
        i = Image.open(f)
        f_name, f_ext = os.path.splitext(f)
        i.thumbnail(size_400) #takes a tuple
        i.save('400/{}_400{}'.format(f_name, f_ext))


# In[16]:


#rotate an image

my_image.show()


# In[6]:


my_image.rotate(90)


# In[18]:


my_image.show()


# In[7]:


#convert the image to black and white

my_image.convert(mode='L') #add .save() to the end to save it


# In[20]:


#add a blur

from PIL import ImageFilter


# In[8]:


my_image.filter(ImageFilter.GaussianBlur()) #not much of blur


# In[9]:


my_image.filter(ImageFilter.GaussianBlur(10))


# In[10]:


#image transformation

output = my_image.transpose(Image.FLIP_LEFT_RIGHT)
output


# In[11]:


output = my_image.transpose(Image.FLIP_TOP_BOTTOM)
output


# In[12]:


output = my_image.transpose(Image.ROTATE_90)
output


# In[13]:


output = my_image.transpose(Image.ROTATE_180)
output


# In[14]:


output = my_image.transpose(Image.ROTATE_270)
output


# In[ ]:




