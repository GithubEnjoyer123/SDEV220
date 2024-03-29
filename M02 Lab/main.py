'''
Name: Justin Phillips
Date: 3/29/2024
File name: main.py
Description: This program is designed to calculate the GPA of students to see if the qualify for the dean's list.
Purpose: Practice using conditionals in python

Variables:
Name is assigned to the string input from the user to enter a students name
gpa is assigned to the float input from the user to assign a GPA including decimal values
'''

while True:
    name = input('\nPlease enter the students name (Enter ZZZ to cancel): ')
    if name == 'ZZZ':
        break
    gpa = float(input('Please enter students GPA: '))
    if gpa >= 3.5:
        print(name + ' has made the Dean\'s list!')
    elif gpa >= 3.25:
        print(name + ' has made the Honor roll!')
    else:
        continue