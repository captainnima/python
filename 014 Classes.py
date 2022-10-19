#!/usr/bin/env python
# coding: utf-8

# In[1]:


#classes allow logical grouping of functions and data (methods and attributes)


# In[2]:


#empty class with no attributes or methods

class Employee:
    pass


# In[3]:


#instances of the class (that is objects)

emp_1 = Employee()
emp_2 = Employee()


# In[4]:


print(emp_1)


# In[5]:


print(id(emp_1))


# In[6]:


#add instance variables to Employee
#instance variables are unique to each instance of the object
#they are in fact called properties


# In[7]:


emp_1.first = 'Bugs'
emp_1.last = 'Bunny'
emp_1.pay = 100000

emp_2.first = 'Daffy'
emp_2.last = 'Duck'
emp_2.pay = 80000


# In[8]:


print(emp_1.first, emp_1.last, emp_1.pay)


# In[10]:


#to avoid setting the variables manually like this,
#we can declare these as instance variables inside
#the class definition

#to do this, we use the __init__ constructor
#when creating corresponding functionality (methods), they receive
#the instance as the first parameter; by convention we call this
#self

#think about it like this: when we write self.first = f, it's like
#earlier when we wrote emp_1.first = 'Bugs'; it's just now that this
#is done automatically in out constructor


class Employee:
    def __init__(self, f, l, p=50000): #construtor method
        self.first = f
        self.last = l
        self.pay = p
        self.email = f + '.' + l + '@company.edu'


# In[11]:


emp_3 = Employee('Porky', 'Pig', 90000)


# In[12]:


print(emp_3.first, emp_3.last, emp_3.pay)


# In[13]:


print(emp_3.email)


# In[16]:


class Employee:
    def __init__(self, first, last, pay=50000): #construtor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.edu'
        
    def full_name(self):
        return self.first + ' ' + self.last


# In[17]:


emp_4 = Employee('Pete', 'Puma')


# In[18]:


print(emp_4.pay)


# In[19]:


emp_4.full_name()


# In[20]:


print(emp_4.full_name())


# In[21]:


class Employee:
    def __init__(self, first, last, pay=50000): #construtor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.edu'
        
    def full_name(self):
        return self.first + ' ' + self.last
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


# In[22]:


emp_5 = Employee('Marvin', 'Martian')


# In[23]:


emp_5.full_name()


# In[24]:


emp_5.pay


# In[25]:


emp_5.apply_raise()


# In[26]:


emp_5.pay


# In[27]:


#working with class variables
#class variables are different from instance variables
#class variables are there for "every" instance of the class
#that is for all objects

class Employee:
    raise_amount = 1.04 #class variable
    
    def __init__(self, first, last, pay=50000): #construtor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.edu'
        
    def full_name(self):
        return self.first + ' ' + self.last
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# In[28]:


emp_6 = Employee('Mickey', 'Mouse', 70000)


# In[29]:


print(emp_6.full_name(), emp_6.pay)


# In[30]:


emp_6.apply_raise()


# In[31]:


print(emp_6.pay)


# In[32]:


Employee.raise_amount = 1.07


# In[33]:


emp_6.apply_raise()


# In[34]:


print(emp_6.pay)


# In[37]:


#print out the name space of an instance
#no mention of the raise_amount variable since it is a class variable
#and not an instance variable

print(emp_6.__dict__)


# In[38]:


temp_emp = Employee('Bernard', 'Mouse', 100000)
print(temp_emp.full_name(), temp_emp.pay)


# In[39]:


temp_emp.apply_raise()


# In[40]:


print(temp_emp.pay)


# In[41]:


#print the class name space; notice that the class variable shows up

print(Employee.__dict__)


# In[42]:


#change the class variable for an instance

print(emp_6.full_name())


# In[43]:


emp_6.raise_amount = 1.10
print(Employee.raise_amount)


# In[44]:


print(emp_6.raise_amount)


# In[45]:


#remember that each instance looks inside itself to see if an attribute
#exists; if not, it checks the parent and so on; in this case, since
#we have emp_6 use rasie_amount, when we print out its name space, the
#attribute shows up since it was changed for it specifically

print(emp_6.__dict__)


# In[46]:


Employee.raise_amount = 1.20


# In[47]:


print(emp_6.__dict__)


# In[48]:


print(emp_6.pay)


# In[49]:


emp_6.apply_raise()


# In[50]:


print(emp_6.pay)


# In[51]:


del emp_6.raise_amount


# In[52]:


print(emp_6.__dict__)


# In[53]:


emp_6.apply_raise()


# In[54]:


print(emp_6.pay)


# In[1]:


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


# In[2]:


emp_7 = Employee('Bianca', 'Mouse', 70000)
emp_8 = Employee('Bernard', 'Mouse', 70000)


# In[3]:


print(Employee.num_of_emps)


# In[4]:


del emp_7


# In[5]:


print(Employee.num_of_emps)


# In[6]:


#decorators

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


# In[9]:


emp_7 = Employee('Bianca', 'Mouse', 100000)
emp_8 = Employee('Bernard', 'Mouse', 100000)


# In[10]:


Employee.set_raise_amount(1.07)


# In[11]:


emp_7.apply_raise()
emp_8.apply_raise()

print(emp_7.pay)
print(emp_8.pay)


# In[12]:


#parsing a string

emp_str_9 = 'Daisy-Duck-50000'

print(emp_str_9.split('-'))


# In[15]:


first, last, pay = emp_str_9.split('-')
emp_9 = Employee(first, last, pay)
print(emp_9.full_name(), emp_9.pay)


# In[16]:


#above works but it is cumbersome

#lets create a new class method to do the work for us

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


# In[17]:


emp_str_10 = 'Tweety-Bird-50000'

emp_10 = Employee.from_string(emp_str_10)
print(emp_10.full_name(), emp_10.pay)


# In[18]:


#static methods
#regular methods automatically pass their instance as an argument (that is the self)
#class methods automatically pass the class as an argument (cls)
#static methods do not pass anything automatically; so they are more or less functions

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


# In[19]:


import datetime


# In[21]:


my_date = datetime.date(2019, 7, 14)
print(Employee.is_workday(my_date))


# In[22]:


my_date = datetime.date(2019, 7, 16)
print(Employee.is_workday(my_date))


# In[ ]:


#inheritance and subclasses
#inheritance allows attributes and methods to be inherited from parents
#we can override the parent classes and subclasses
#we can also add addtional functionality


# In[24]:


#create a new inherited class

class Developer(Employee):
    pass


# In[25]:


dev_1 = Developer('Bugs', 'Bunny', 10000)
print(dev_1.full_name(), dev_1.pay, dev_1.email)


# In[26]:


#use the help() to show the method resolution order

print(help(Developer))


# In[27]:


#we want Developers to have a 10% raise

class Developer(Employee):
    raise_amount = 1.10


# In[28]:


dev_1 = Developer('Bugs', 'Bunny', 10000)
emp_1 = Employee('Daffy', 'Duck', 10000)


# In[29]:


dev_1.apply_raise()
emp_1.apply_raise()


# In[30]:


print(dev_1.pay)
print(emp_1.pay)


# In[31]:


#we want to pass the main programming language of the developer as a parameter

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


# In[32]:


dev_1 = Developer('Bugs', 'Bunny', 10000, 'Python')
emp_1 = Employee('Daffy', 'Duck', 10000)


# In[33]:


print(dev_1.full_name(), dev_1.email, dev_1.prog_lang)


# In[34]:


#create Managers

class Manager(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            
    def print_employees(self):
        for employee in self.employees:
            print('-->', employee.full_name(), employee.email)


# In[35]:


dev_1 = Developer('Bugs', 'Bunny', 100000, 'Python')
dev_2 = Developer('Marvin', 'Martian', 80000, 'C++')
emp_1 = Employee('Charlie', 'Dog', 70000)
mgr_1 = Manager('Porky', 'Pig', 90000, [dev_1, dev_2, emp_1])


# In[36]:


print(mgr_1.email)


# In[37]:


mgr_1.print_employees()


# In[38]:


dev_3 = Developer('Daffy', 'Duck', 80000, 'Java')
dev_4 = Developer('Pete', 'Puma', 80000, 'Ada')
emp_2 = Employee('Bianca', 'Mouse', 90000)
emp_3 = Employee('Bernard', 'Mosue', 90000)


# In[39]:


mgr_1.add_employee(dev_3)
mgr_1.add_employee(dev_4)
mgr_1.add_employee(emp_2)
mgr_1.add_employee(emp_3)


# In[40]:


mgr_1.print_employees()


# In[41]:


mgr_1.remove_employee(dev_3)


# In[42]:


mgr_1.print_employees()


# In[43]:


print(dev_1.full_name())


# In[44]:


mgr_1.add_employee(dev_1)


# In[45]:


mgr_1.print_employees()


# In[46]:


#two built-in functions for working with classes
#isinstance() and issubclass()


# In[47]:


print(isinstance(mgr_1, Employee))


# In[48]:


print(isinstance(mgr_1, Developer))


# In[49]:


print(issubclass(mgr_1, Employee))


# In[50]:


print(issubclass(Manager, Employee)) #correct way of writing it


# In[51]:


print(issubclass(Developer, Manager))


# In[ ]:




