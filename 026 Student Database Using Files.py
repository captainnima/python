#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Student Database Using Files
#a database for keeping track of a class and its students

import sys


# In[6]:


class Student:
    #constructor and attributes
    def __init__(self, identity, name, email, grade=0):
        self.identity = identity
        self.name = name
        self.email = email
        self.grade = grade
        
    #methods
    def fetchStudent(self):
        studentInfo = (self.identity, self.name, self.email, self.grade)
        return studentInfo
    
    def setGrade(self, g):
        self.grade = g
        
def menu():
    print()
    print('Main Menu')
    print()
    print('1. Print roster')
    print('2. Fetch a student by Id')
    print('3. Change a student grade by Id')
    print('4. Assign grades to everyone')
    print('5. Drop a student from class')
    print('6. Add a student to class')
    print('q. Quit the program')
    print()

def printRoster(storage):
    print()
    print('Class Roster')
    for s in storage:
        print(s.fetchStudent())
        
def fetchStudentById(storage):
    print()
    sId = int(input('Enter a student Id: '))
    found = False
    for s in storage:
        if s.fetchStudent()[0] == sId:
            print(s.fetchStudent())
            found = True
            break
    if found == False:
        print('No student by that Id')

def changeGradeById(storage):
    print()
    sId = int(input('Enter a student Id: '))
    found = False
    for s in storage:
        if s.fetchStudent()[0] == sId:
            print(s.fetchStudent())
            numericGrade = int(input('Enter student numeric Grade: '))
            s.setGrade(numericGrade)
            found = True
            break
    if found == False:
        print('No student by that Id')
        
def assignGrades(storage):
    print()
    for s in storage:
        print(s.fetchStudent())
        numericGrade = int(input('Enter student numeric grade: '))
        s.setGrade(numericGrade) #assign grade
        
def dropStudentById(storage):
    print()
    sId = int(input('Enter a student Id: '))
    found = False
    for s in storage:
        if s.fetchStudent()[0] == sId:
            found = True
            print(s.fetchStudent())
            print()
            confirm = input('Are you sure you want to drop this student?(y/n) ')
            if confirm.lower() == 'y':
                storage.remove(s)
                print('Student dropped')
                break
            else:
                print('Operation cancelled')
                break
    if found == False:
        print('No student by that Id')
    
def addStudent(storage):
    print()
    sId = int(input('Enter the student Id (4 digits): '))
    sName = input('Enter the student name: ')
    sEmail = input('Enter the student email: ')
    
    #create a new Student object with the values and add it to my list
    newStudent = Student(sId, sName, sEmail)
    storage.append(newStudent)
    print('Student added to the database successfully')
    
def processRequest(selection, storage):
    if selection == '1':
        printRoster(storage)
    elif selection == '2':
        fetchStudentById(storage)
    elif selection == '3':
        changeGradeById(storage)
    elif selection == '4':
        assignGrades(storage)
    elif selection == '5':
        dropStudentById(storage)
    elif selection == '6':
        addStudent(storage)
    else:
        return 'q'
    
def main():
    print('Welcome to the student database')
    className = input('What is the class name? ')
    instructor = input('Who is the instructor? ')
    fileName = className.replace(' ', '') + '.txt'
    storage = [] #empty list
    
    #read from an existing file if one is there
    try:
        infile = open(fileName, 'r')
        for line in infile.readlines():
            temp = line.split(',')
            sId = int(temp[0])
            sName = temp[1]
            sEmail = temp[2]
            sGrade = int(temp[3].replace('\n', ''))
            newStudent = Student(sId, sName, sEmail, sGrade)
            storage.append(newStudent)
        infile.close()   
    except:
        pass
    
    selection = ''
    while selection != 'q':
        menu()
        selection = input('Make a selection: ')
        response = processRequest(selection, storage)
        if response == 'q':
            break
    
    #write the list to a file
    outfile = open(fileName, 'w')
    
    for s in storage:
        print(s.fetchStudent()[0], file=outfile, end=',')
        print(s.fetchStudent()[1], file=outfile, end=',')
        print(s.fetchStudent()[2], file=outfile, end=',')
        print(s.fetchStudent()[3], file=outfile, end='\n')
        
    outfile.close()
            
main()


# In[2]:


text = 'This is a piece of text'
text.replace(' ', '') + '.txt'


# In[3]:


item = '1234,Bugs Bunny,bbunny@gwu.edu,0'
item.split(',')


# In[ ]:




