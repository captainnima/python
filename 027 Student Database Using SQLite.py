#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sys
import sqlite3


# In[7]:


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


# In[11]:


def findStudent(storage):
    print()
    sId = int(input('Enter a student Id: '))
    found = False
    for s in storage:
        if s.fetchStudent()[0] == sId:
            found = True
            print(s.fetchStudent())
            return s
    if found == False:
        print('No student by that Id')
        return False
    
def printRoster(storage):
    print()
    print('Class Roster')
    for s in storage:
        print(s.fetchStudent())
        
def fetchStudentById(storage):
    print()
    findStudent(storage)
    
def changeGradeById(storage, db):
    print()
    response = findStudent(storage)
    if response != False:
        numericGrade = int(input('Enter a student grade in numeric form: '))
        response.setGrade(numericGrade)
        db.execute('update student set s_grade = ? where s_id = ?', (numericGrade, response.identity))
        db.commit()
        print()
        print('Student grade updated')
        
def assignGrades(storage, db):
    print()
    for s in storage:
        print(s.fetchSudent())
        numericGrade = int(input('Enter a student grade in numeric form: '))
        s.setGrade(numericGrade)
        db.execute('update student set s_grade = ? where s_id = ?', (numericGrade, s.identity))
        db.commit()
        
def dropStudentById(storage, db):
    print()
    response = findStudent(storage)
    if response != False:
        confirm = input('Are you sure you want to drop this student? (y/n) ')
        if confirm.lower() == 'y':
            db.execute('delete from student where s_id = ?', (response.identity,))
            db.commit()
            storage.remove(response)
            print('Student dropped')
        else:
            print('Operation cancelled')
            
def addStudent(storage, db):
    print()
    sId = int(input('Enter a student Id (4 digits): '))
    sName = input('Enter a student name: ')
    sEmail = input('Enter student email: ')
    
    #create the student object, add it to the list and to the database
    newStudent = Student(sId, sName, sEmail)
    storage.append(newStudent)
    temp = newStudent.fetchStudent()
    db.execute('insert into student (s_id, s_name, s_email, s_grade) values(?,?,?,?)', temp)
    db.commit()
    print('Student added successfully')
    


# In[12]:


def processRequest(selection, storage, db):
    if selection == '1':
        printRoster(storage)
    elif selection == '2':
        fetchStudentById(storage)
    elif selection == '3':
        changeGradeById(storage, db)
    elif selection == '4':
        assignGrades(storage, db)
    elif selection == '5':
        dropStudentById(storage, db)
    elif selection == '6':
        addStudent(storage, db)
    else:
        return 'q'


# In[14]:


def main():
    print('Welcome to the student database')
    className = input('What is the class name? ')
    instructor = input('Who is the instructor? ')
    className = className.replace(' ', '') + '.db' #SQLite database
    storage = []
    
    db = sqlite3.connect(className) #connection to the database
    
    #call the database and execute some SQL statements
    
    try:
        db.execute('create table student (s_id int, s_name text, s_email text, s_grade int)')
    except:
        pass
    
    try:
        cursor = db.execute('select * from student')
        for row in cursor:
            sId = row[0]
            sName = row[1]
            sEmail = row[2]
            sGrade = row[3]
            newStudent = Student(sId, sName, sEmail, sGrade)
            storage.append(newStudent)
    except:
        pass
    
    selection = ''
    while selection != 'q':
        menu()
        selection = input('Make a selection: ')
        response = processRequest(selection, storage, db)
        if response == 'q':
            break
    
    
main()


# In[ ]:




