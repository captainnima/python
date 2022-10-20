#!/usr/bin/env python
# coding: utf-8

# In[2]:


#dunder methods
#these are special methods surrounded by __ (double underscores)
#they allow emulation of some of the built-in behavior in Python
#they also allow for method overloading and overriding

class Employee:
    raise_amount = 1.04 #class variable
    num_of_emps = 0 #number of employees
    
    def __init__(self, first, last, pay=50000): #construtor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.edu'
        
        Employee.num_of_emps += 1 #add 1 each time a new employee is added
                                  #notice the Employee class sicne we do not
                                  #want the total number of employees to be
                                  #different for every instance
        
    def __del__(self):
        Employee.num_of_emps -= 1
        
    def full_name(self):
        return self.first + ' ' + self.last
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod    #class method for all instances
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #create the object and return it
    
    @staticmethod #static method to determine if a day is a workday
    def is_workday(day):
        if (day.weekday() == 5 or day.weekday() == 6):
            return False
        else:
            return True


# In[3]:


#method overloading; the + operator behaves differently for numbers and strings

print(1+2)
print('a' + 'b')


# In[9]:


emp_1 = Employee('Bugs', 'Bunny', 100000)


# In[5]:


print(emp_1)


# In[8]:


class Employee:
    raise_amount = 1.04 #class variable
    num_of_emps = 0 #number of employees
    
    def __init__(self, first, last, pay=50000): #construtor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.edu'
        
        Employee.num_of_emps += 1 #add 1 each time a new employee is added
                                  #notice the Employee class sicne we do not
                                  #want the total number of employees to be
                                  #different for every instance
        
    def __del__(self):
        Employee.num_of_emps -= 1
        
    def full_name(self):
        return self.first + ' ' + self.last
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    #adding __repr__
    #allow for a better representation of the object when printed
    def __repr__(self):
        return "Employee('{}, {}, {}')".format(self.first, self.last, self.pay)
        
        
    @classmethod    #class method for all instances
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #create the object and return it
    
    @staticmethod #static method to determine if a day is a workday
    def is_workday(day):
        if (day.weekday() == 5 or day.weekday() == 6):
            return False
        else:
            return True


# In[10]:


print(emp_1) #__repr__ makes the output be this instead of the default


# In[14]:


class Employee:
    raise_amount = 1.04 #class variable
    num_of_emps = 0 #number of employees
    
    def __init__(self, first, last, pay=50000): #construtor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.edu'
        
        Employee.num_of_emps += 1 #add 1 each time a new employee is added
                                  #notice the Employee class sicne we do not
                                  #want the total number of employees to be
                                  #different for every instance
        
    def __del__(self):
        Employee.num_of_emps -= 1
        
    def full_name(self):
        return self.first + ' ' + self.last
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    #adding __repr__
    #allow for a better representation of the object when printed
    def __repr__(self):
        return "Employee('{}, {}, {}')".format(self.first, self.last, self.pay)
        
    #__str__ actually calls __repr__
    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)
    
    
    @classmethod    #class method for all instances
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #create the object and return it
    
    @staticmethod #static method to determine if a day is a workday
    def is_workday(day):
        if (day.weekday() == 5 or day.weekday() == 6):
            return False
        else:
            return True


# In[15]:


emp_1 = Employee('Bugs', 'Bunny', 100000)


# In[16]:


print(emp_1)


# In[17]:


print(repr(emp_1))


# In[18]:


print(str(emp_1))


# In[21]:


#when calling repr() and str() above, they are calling the corresponding
#__repr__() and __str__()

print(emp_1.__repr__())
print(emp_1.__str__())


# In[22]:


#addition example

print(1+2)


# In[23]:


print(int.__add__(1,2))


# In[24]:


class Employee:
    raise_amount = 1.04 #class variable
    num_of_emps = 0 #number of employees
    
    def __init__(self, first, last, pay=50000): #construtor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.edu'
        
        Employee.num_of_emps += 1 #add 1 each time a new employee is added
                                  #notice the Employee class sicne we do not
                                  #want the total number of employees to be
                                  #different for every instance
        
    def __del__(self):
        Employee.num_of_emps -= 1
        
    def full_name(self):
        return self.first + ' ' + self.last
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    #adding __repr__
    #allow for a better representation of the object when printed
    def __repr__(self):
        return "Employee('{}, {}, {}')".format(self.first, self.last, self.pay)
        
    #__str__ actually calls __repr__
    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)
    
    #adding two employees together
    #our definition: adding their salaries
    def __add__(self, other):
        return self.pay + other.pay
    
    @classmethod    #class method for all instances
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #create the object and return it
    
    @staticmethod #static method to determine if a day is a workday
    def is_workday(day):
        if (day.weekday() == 5 or day.weekday() == 6):
            return False
        else:
            return True


# In[25]:


emp_1 = Employee('Bugs', 'Bunny', 100000)
emp_2 = Employee('Daffy', 'Duck', 70000)


# In[26]:


print(emp_1.full_name(), emp_1.pay)
print(emp_2.full_name(), emp_2.pay)


# In[27]:


print(emp_1 + emp_2)


# In[28]:


#issues with changing an attribute

print(emp_1.first)
print(emp_1.full_name())
print(emp_1.email)


# In[29]:


emp_1.first = 'Babs'


# In[30]:


print(emp_1.first)
print(emp_1.full_name())
print(emp_1.email)


# In[31]:


#notice the email didn't change
#this is because the email is based on the first and last names
#when the object is created


# In[32]:


#let's do this using a method call

class Employee:
    raise_amount = 1.04 #class variable
    num_of_emps = 0 #number of employees
    
    def __init__(self, first, last, pay=50000): #construtor method
        self.first = first
        self.last = last
        self.pay = pay
        
        Employee.num_of_emps += 1 #add 1 each time a new employee is added
                                  #notice the Employee class sicne we do not
                                  #want the total number of employees to be
                                  #different for every instance
        
    def __del__(self):
        Employee.num_of_emps -= 1
        
    def full_name(self):
        return self.first + ' ' + self.last
    
    def email(self):
        return self.first + '.' + self.last + '@companyname.edu'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    #adding __repr__
    #allow for a better representation of the object when printed
    def __repr__(self):
        return "Employee('{}, {}, {}')".format(self.first, self.last, self.pay)
        
    #__str__ actually calls __repr__
    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)
    
    #adding two employees together
    #our definition: adding their salaries
    def __add__(self, other):
        return self.pay + other.pay
    
    @classmethod    #class method for all instances
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #create the object and return it
    
    @staticmethod #static method to determine if a day is a workday
    def is_workday(day):
        if (day.weekday() == 5 or day.weekday() == 6):
            return False
        else:
            return True


# In[33]:


emp_1 = Employee('Bugs', 'Bunny', 100000)
emp_2 = Employee('Daffy', 'Duck', 70000)


# In[35]:


print(emp_1.first)
print(emp_1.full_name())
print(emp_1.email())


# In[36]:


emp_1.first = 'Babs'


# In[37]:


print(emp_1.first)
print(emp_1.full_name())
print(emp_1.email())


# In[42]:


#while the above works, it requires all subsequent code be changed;
#all print(emp_1.email) for instances must be changed to print(emp_1.email())
#to solve this issue, let's use a decorator

#let's do this using a method call

class Employee:
    raise_amount = 1.04 #class variable
    num_of_emps = 0 #number of employees
    
    def __init__(self, first, last, pay=50000): #construtor method
        self.first = first
        self.last = last
        self.pay = pay
        
        Employee.num_of_emps += 1 #add 1 each time a new employee is added
                                  #notice the Employee class sicne we do not
                                  #want the total number of employees to be
                                  #different for every instance
        
    def __del__(self):
        Employee.num_of_emps -= 1
     
    @property
    def full_name(self):
        return self.first + ' ' + self.last
    
    @property #treat this as a property
    def email(self):
        return self.first + '.' + self.last + '@companyname.edu'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    #adding __repr__
    #allow for a better representation of the object when printed
    def __repr__(self):
        return "Employee('{}, {}, {}')".format(self.first, self.last, self.pay)
        
    #__str__ actually calls __repr__
    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)
    
    #adding two employees together
    #our definition: adding their salaries
    def __add__(self, other):
        return self.pay + other.pay
    
    @classmethod    #class method for all instances
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #create the object and return it
    
    @staticmethod #static method to determine if a day is a workday
    def is_workday(day):
        if (day.weekday() == 5 or day.weekday() == 6):
            return False
        else:
            return True


# In[43]:


emp_1 = Employee('Bugs', 'Bunny', 100000)
emp_2 = Employee('Daffy', 'Duck', 70000)


# In[45]:


print(emp_1.first)
print(emp_1.full_name)
print(emp_1.email)


# In[46]:


emp_1.first = 'Babs'


# In[47]:


print(emp_1.first)
print(emp_1.full_name)
print(emp_1.email)


# In[48]:


#another issue
#@property decorator works great but we can't set anything with it

emp_1.full_name = 'Porky Pig'


# In[50]:


#while the above works, it requires all subsequent code be changed;
#all print(emp_1.email) for instances must be changed to print(emp_1.email())
#to solve this issue, let's use a decorator

#let's do this using a method call

class Employee:
    raise_amount = 1.04 #class variable
    num_of_emps = 0 #number of employees
    
    def __init__(self, first, last, pay=50000): #construtor method
        self.first = first
        self.last = last
        self.pay = pay
        
        Employee.num_of_emps += 1 #add 1 each time a new employee is added
                                  #notice the Employee class sicne we do not
                                  #want the total number of employees to be
                                  #different for every instance
        
    def __del__(self):
        Employee.num_of_emps -= 1
     
    @property
    def full_name(self):
        return self.first + ' ' + self.last
    
    @full_name.setter #add this
    def full_name(self, name):
        first, last = name.split() #nothing passed uses space to split
        self.first = first
        self.last = last
    
    @property #treat this as a property
    def email(self):
        return self.first + '.' + self.last + '@companyname.edu'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    #adding __repr__
    #allow for a better representation of the object when printed
    def __repr__(self):
        return "Employee('{}, {}, {}')".format(self.first, self.last, self.pay)
        
    #__str__ actually calls __repr__
    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)
    
    #adding two employees together
    #our definition: adding their salaries
    def __add__(self, other):
        return self.pay + other.pay
    
    @classmethod    #class method for all instances
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #create the object and return it
    
    @staticmethod #static method to determine if a day is a workday
    def is_workday(day):
        if (day.weekday() == 5 or day.weekday() == 6):
            return False
        else:
            return True


# In[51]:


emp_1 = Employee('Bugs', 'Bunny', 100000)
emp_2 = Employee('Daffy', 'Duck', 70000)


# In[52]:


print(emp_1.first)
print(emp_1.full_name)
print(emp_1.email)


# In[53]:


emp_1.full_name = 'Porky Pig'


# In[54]:


print(emp_1.first)
print(emp_1.full_name)
print(emp_1.email)


# In[55]:


emp_1.full_name()


# In[ ]:




