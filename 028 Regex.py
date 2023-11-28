#!/usr/bin/env python
# coding: utf-8

# # 028 Regex

# In[1]:


#working with re library and regular expressions;
#regular expressions look daunting at first;
#they get easy very quickly if used often

import re


# In[2]:


text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Hi HiHi HiHo

Meta characters (need to be escaped using \):
. ^ $ + ? { } [ ] \ | ( )

bbunny@looney.com
dduck@looney.com
joey1234@gwu.edu
joey.awesome@isp.net
moscow.mitch@kremlin.gov.ru

looney@com

https://www.google.com
http://www.florida-dreaming.com
https://youtube.com
https://www.nasa.gov

703,555,1717
703-555-1313
407.555.1313
703-555-1212
800-555-1212
900-555-1212

301--555-1212

cat
mat
pat
hat
bat

Dr. Bugs Bunny
Mr. Daffy Duck
Mr Porky Pig
Ms Drumpf
Mr. T
Dr. Z
Mrs. Daisy Duck
Hello World
'''

sentence = "Eagles don't flock. Pigeons do. Pigeons in Central Park"


# In[5]:


#raw strings: just a string prefixed with r;
#it tells Python not to treat backslashes in any special way

print("\tThis is a Tab")


# In[6]:


print(r'\tThis is a Tab')


# In[ ]:


#we will use the re compile() method;
#this method allows us to precompile the regex
#and store it as a variable for later pattern matching


# In[7]:


#search for a pattern; searches are case sensitive

pattern = re.compile(r'abc')


# In[8]:


pattern


# In[9]:


#search for the pattern

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[10]:


#we found a single match; a closer look

print(text_to_search[1:4])


# In[11]:


pattern = re.compile(r'looney')


# In[12]:


#search for the pattern

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[13]:


print(text_to_search[161:167], text_to_search[178:184])


# In[14]:


#searching for a period, .; periods have special meaning

pattern = re.compile(r'.')


# In[15]:


matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[16]:


pattern = re.compile(r'\.')


# In[17]:


matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[18]:


pattern = re.compile(r'looney.com')


# In[19]:


matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[20]:


pattern = re.compile(r'looney\.com')


# In[21]:


matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# ## Special Characters
.       -Any character except new line
\d      -Digit (0-9)
\D      -Not a digit (0-9)
\w      -Word character (a-z, A-Z, 0-9, _)
\W      -Not a word character
\s      -White space (space, tab, new line)
\S      -Not a white space


anchors: they don't match characters but can be used before and after characters

\b      -Word boundary (marked by white space or non alphanumeric characters)
\B      -Not a word boundary
^       -Beginning of a string; if used inside a character set ([ ]), means negation
$       -End of a string

[]      -character set (matches characters in the brackets, a single match only)
[^ ]    -Matches characters NOT in the brackets

|       -Either or
()      -Group or grouping



quantifiers: for selecting more than a single character

*       -0 or more
+       -more than 1
?       -0 or 1
{3}     -Exact number
{3,8}   -Range of numbers {min,max}


sample regex:

email: [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
# In[22]:


#let's look at these special characters;
#. matches everything except new lines

pattern = re.compile(r'.')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[23]:


#digits \d

pattern = re.compile(r'\d')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[24]:


pattern = re.compile(r'\d\d\d')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[25]:


#not digits \D

pattern = re.compile(r'\D')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[26]:


#word character \w

pattern = re.compile(r'\w')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[27]:


#not a word character \W

pattern = re.compile(r'\W')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[28]:


#white space \s

pattern = re.compile(r'\s')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[29]:


#not white space \S

pattern = re.compile(r'\S')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[34]:


#word bounday \b for "Hello World"

pattern = re.compile(r'\bHello World')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[35]:


#not a word boundary \B for "Hello World"

pattern = re.compile(r'\BHello World')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# In[36]:


#^ for beginning of a string

pattern = re.compile(r'^Eagles')

matches = pattern.finditer(sentence) #change to sentence
for match in matches:
    print(match)


# In[37]:


pattern = re.compile(r'^Park')

matches = pattern.finditer(sentence) #change to sentence
for match in matches:
    print(match)


# In[38]:


#$ for ending of a string

pattern = re.compile(r'Park$')

matches = pattern.finditer(sentence) #change to sentence
for match in matches:
    print(match)


# In[39]:


#matching the phone numbers;
#using a character set []; matches one or another; single match
#notice the 301 number is missing since it has --

#first a simple approach

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[40]:


#bit more precision

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[41]:


#using an external file

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

#adjust to open('contacts.csv', 'r')
with open('contacts.csv', 'r') as f: #add encoding='utf-8' if errors
    contents = f.read()
    matches = pattern.finditer(contents) #change to external file

    for match in matches:
        print(match)


# In[42]:


#expanding the search

pattern = re.compile(r'\d\d\d[-.]+\d\d\d[-.]+\d\d\d\d')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[43]:


#suppose we want to match 800 and 900 numbers only

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[44]:


#range operator, -

pattern = re.compile(r'[1-5]') #same as [12345]

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[45]:


pattern = re.compile(r'[f-n]') #same as [fghijklmn]

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[46]:


pattern = re.compile(r'[f-nF-L]') #remember it is a single match

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[47]:


#range operator, -, using ^ for negation

pattern = re.compile(r'[^a-c]')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[52]:


#matching cat, mat, pat, hat, but not bat

pattern = re.compile(r'[^b]at')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[53]:


#so far everything we have done only looks at single
#character matches; we can use quantifiers to match
#more than one character

#the old way

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[54]:


#the new way using quantifiers

pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[55]:


#matching the titles

pattern = re.compile(r'Mr')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[56]:


pattern = re.compile(r'Mr\.')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[57]:


pattern = re.compile(r'Mr\.?') #? means 0 or 1

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[58]:


pattern = re.compile(r'Mr\.?\s[A-Z]\w+') #notice not everyone shows up

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[59]:


pattern = re.compile(r'Mr\.?\s[A-Z]\w*') #replace + with *

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[61]:


#using groups to get more results
#groups use (); use pipe for or

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') #notice everyone shows up

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[62]:


#another way, perhaps clearer

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') #notice everyone shows up

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[63]:


#use groups to also pick up Dr.

pattern = re.compile(r'(M|D)(r|s|rs)\.?\s[A-Z]\w*') #notice not everyone shows up

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[64]:


#fetching some emails

pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[65]:


pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu|net)')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[66]:


pattern = re.compile(r'[a-zA-Z0-9.]+@[a-zA-Z]+\.(com|edu|net)')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[67]:


#the + inside the character set ([]) acts like a regular character
#the + outside the brackets means 1 or more matches

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[68]:


#fetching domain names from URLs using groups;
#recall that ? means 0 or 1; it makes something be optional

#below almost works; florida-dreaming.com doesn't show

pattern = re.compile(r'https?://(www\.)?\w+\.\w+')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[69]:


pattern = re.compile(r'https?://(www\.)?(\w+)-?\w+\.\w+')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match)


# In[70]:


#these groups are indexed; we can look at them using their indexes

pattern = re.compile(r'https?://(www\.)?(\w+-?\w+)(\.\w+)')

matches = pattern.finditer(text_to_search) #change to text_to_search
for match in matches:
    print(match.group(0)) #group index: 0 is the whole URL
    print(match.group(1)) #group index: 1 is the www or lack of
    print(match.group(2)) #group index: 2 is the domain name
    print(match.group(3)) #group index: 3 is the top level domain name


# In[71]:


urls = '''
https://www.google.com
http://www.florida-dreaming.com
https://youtube.com
https://www.nasa.gov
'''


# In[72]:


#regex has a sub method for back references

pattern = re.compile(r'https?://(www\.)?(\w+-?\w+)(\.\w+)')

#pass in the back references;
#a \ with the group number

sub_urls = pattern.sub(r'\2\3', urls)


# In[73]:


print(sub_urls)


# In[74]:


#so far we have been using finditer(); we can also use findall();
#findall() returns a string list of matches;
#finditer() does return additional information

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w+')

matches = pattern.findall(text_to_search)
for match in matches:
    print(match)


# In[75]:


matches #notice it returns a list


# In[76]:


pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')

matches = pattern.findall(text_to_search)
for match in matches:
    print(match)


# In[77]:


#using the search() method to find a pattern;
#finds the first one and stops

pattern = re.compile(r'Pigeons')

matches = pattern.search(sentence)
print(matches)


# In[78]:


#using flags;
#let's say we want to search for match regardless of case

pattern = re.compile(r'pigeons', re.IGNORECASE) # I works too

matches = pattern.search(sentence)
print(matches)


# In[ ]:




