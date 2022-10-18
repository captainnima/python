#!/usr/bin/env python
# coding: utf-8

# In[1]:


#retirement calculator

import math


# In[9]:


principle = float(input('Enter your principle: '))
interest = float(input('Enter the interest rate like 7.5: '))
interest = interest / 100
years = float(input('Enter number of years before retirement: '))
contribution = float(input('Enter monthly contibution amount: '))

retirement_no_contribution = round(principle*math.pow((1+interest/4), 4*years), 2)

retirement_with_contribution = round(contribution*((math.pow((1+interest/4), 4*years)-1)                                              / (interest/years)) * (1+interest/years), 2)

print('Your retirement with no contribution is {}'.format(retirement_no_contribution))
print('Your retirement with contribution is {}'.format(retirement_with_contribution))


# In[ ]:




