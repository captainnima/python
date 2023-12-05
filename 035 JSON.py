#!/usr/bin/env python
# coding: utf-8

# # 035 JSON

# In[1]:


#JSON is JavaScript Object Notation

import json


# In[2]:


#key called people with value of an array of objects
#double quotes required in json

people_string = '''
    {
        "people": [
            {
                "name":"Bugs Bunny",
                "phone": "703-555-1212",
                "emails": ["bbunny@navy.mil", "bbunny@looney.com"],
                "has_license": true
            },
            {
                "name":"Daffy Duck",
                "phone": "703-555-1313",
                "emails": null,
                "has_license": false                
            }
        ]
    }
'''


# In[3]:


print(people_string)


# In[4]:


#json read of a string returns a dictionary

data = json.loads(people_string) #loads is read "load s"; requires a string


# In[5]:


print(data)


# In[6]:


print(type(data))


# In[ ]:


#python json encoders/decoders

#https://docs.python.org/3/library/json.html
#be sure to scroll down a little to see the chart


# In[7]:


#verify that the conversions are correct
print(type(['people']))


# In[8]:


#looping through

for person in data['people']:
    print(person)


# In[9]:


#more loops

for person in data['people']:
    print(person['name'])


# In[10]:


#let's reverse the process and dump a Python object
#into a json string

#let's remove the phone number key and values prior

for person in data['people']:
    del person['phone']


# In[11]:


for person in data['people']:
    print(person)


# In[12]:


#let's dump the rest into a string

new_string = json.dumps(data)
print(new_string)


# In[13]:


print(type(new_string))


# In[14]:


#new_string is a json string but doesn't look like it
#let's correct this

new_string = json.dumps(data, indent=2) #indent every level 2 spaces
print(new_string)


# In[15]:


#let's sort keys

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)


# In[16]:


#reading a json file

json_file = open('states.json', 'r')
data = json.load(json_file) #note that it is load and not loads


# In[17]:


print(data)


# In[18]:


for state in data['states']:
    print(data)


# In[19]:


for state in data['states']:
    print(state['name'], state['abbreviation'])


# In[20]:


#let's remove the area code and then write the rest back to a file

for state in data['states']:
    del state['area_codes']


# In[21]:


for state in data['states']:
    print(state)


# In[22]:


new_json = open('states_json.json', 'w')
json.dump(data, new_json)
new_json.close()


# In[23]:


#let's indent the file properly

new_json = open('states_json.json', 'w')
json.dump(data, new_json, indent=2)
new_json.close()


# In[24]:


#real world example

import json
from urllib.request import urlopen


# In[25]:


with urlopen("http://citibikenyc.com/stations/json") as response:
    source = response.read() #get the response from the website
    
data = json.loads(source)
print(json.dumps(data, indent=2))


# In[ ]:


data['executionTime']


# In[ ]:


data['stationBeanList']


# In[ ]:


data['stationBeanList'][0:3]


# In[26]:


#another example

get_ipython().system('pip install yahoofinancials')


# In[27]:


from yahoofinancials import YahooFinancials

currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']
yahoo_financials_currencies = YahooFinancials(currencies)
print(yahoo_financials_currencies.get_historical_price_data("2018-08-01", "2018-08-10", "daily"))


# In[28]:


data = yahoo_financials_currencies.get_historical_price_data("2018-08-01", "2018-08-10", "daily")


# In[29]:


data


# In[30]:


print(json.dumps(data, indent=2))


# In[ ]:




