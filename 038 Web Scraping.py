#!/usr/bin/env python
# coding: utf-8

# # 038 Web Scraping

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


#load a page

r = requests.get("https://www.yellowpages.com/search?search_terms=Coffee&geo_location_terms=Washington%2C+DC")
r


# In[3]:


r.content


# In[4]:


#create a soup variable and read in the content

soup = BeautifulSoup(r.content)


# In[5]:


print(soup)


# In[6]:


print(soup.prettify())


# In[7]:


#list all the anchor tags (<a>)

soup.find_all("a")


# In[8]:


#get all the h1 tags

soup.find_all("h1")


# In[9]:


#show all the links

for link in soup.find_all("a"):
    print(link.get("href"), '*****', link.text)


# In[10]:


#get all the links and display in proper format

for link in soup.find_all("a"):
    print("<a href='%s'>%s</a>" %(link.get("href"), link.text))


# In[11]:


for link in soup.find_all("a"):
    print("<a href='{}'>{}</a>".format(link.get("href"), link.text))


# In[12]:


#create a soup variable and get the coffee stores' information

g_data = soup.find_all("div", attrs={"class":"info"})
g_data


# In[13]:


for item in g_data:
    print(item.text)


# In[14]:


#get items as a list

for item in g_data:
    print(item.contents)


# In[15]:


#print the 0th element content and text

for item in g_data:
    print(item.contents[0])
    
print('**************************')

for item in g_data:
    print(item.contents[0].text)


# In[17]:


#get the name and address of the places

for item in g_data:
    print(item.contents[0].text)
    print(item.contents[1].text)


# In[18]:


#get more specific using the class and build a list

for item in g_data:
    print(item.contents[0].find_all("a", attrs={"class":"business-name"})[0].text)
    print(item.contents[1].find_all("div", {"class":"street-address"})[0].text)
    print(item.contents[1].find_all("div", {"class":"locality"})[0].text)
    print(item.contents[1].find_all("div", attrs={"class":"phones"})[0].text) #attrs is optional
    print()


# In[21]:


import csv

csvfile = open('eggs.csv', 'w')
spamwriter = csv.writer(csvfile, delimiter=',')
spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


# In[27]:


import csv

coffeefile = open('coffee.csv', 'w')
coffeewriter = csv.writer(coffeefile, delimiter=',')

coffeewriter.writerow(["Coffee Shop", "Address", "City", "Phone"])
for item in g_data:
    item1 = item.contents[0].find_all("a", attrs={"class":"business-name"})[0].text
    print(item1)
    item2 = item.contents[1].find_all("div", {"class":"street-address"})[0].text
    print(item2)
    item3 = item.contents[1].find_all("div", {"class":"locality"})[0].text
    print(item3)
    item4 = item.contents[1].find_all("div", attrs={"class":"phone"})[0].text
    print(item4) #attrs is optional
    print()
    coffeewriter.writerow([item1, item2, item3, item4])
    
coffeefile.close()


# In[ ]:





# In[ ]:




