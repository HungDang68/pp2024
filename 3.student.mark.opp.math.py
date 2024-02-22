import numpy as np
import math
import curses
from curses import wrapper

class classes():
    def __init__(self,n,i,cre):
       self.__couse=n
       self.__id=i
       self.__credit=cre
       self.__students= np.array([])
    
    def grade_input(self,grade):
        self.__students=np.append(self.__students,grade)
    
    def __str__(self):
        return f"Name: {self.__couse}   {self.__students}"
    
    def get_credit(self):
        return self.__credit
    
    def get_grade(self,NUM):
        return np.dot(self.__students[NUM],self.__credit)
    
class student:  
    def __init__(self,n,i,dob):
        self.__students=n
        self.__id=i
        self.__Dob=dob
        self.__gpa=float
    
    def __str__(self):
        return f'Name: {self.__students} ID: {self.__id} DoB: {self.__Dob} GPA: {self.__gpa}'
        
    def get_name(self):
        return self.__students
    
    def grade_input(self,grade):
        self.__gpa=grade
        
    def get_grade(self):
        return self.__gpa

def int_input(string):
    while(True):
      try:
        n=float(input(f'{string}'))
        return n
      except Exception as x:
            print("Try again")
            
List_student=[]
List_class=[]
total_credit=0
student_num=0
class_num=0
sorted_student=[]

student_num=int(int_input('Please type in a number of students: '))
print('------------------------------------------')
class_num=int(int_input('Please type in a number of classes: '))
 
for n in range(student_num):
    print('------------------------------------------')
    List_student.append(student(input(f'Pls type in the student number {n+1}\'s name: '),input(f'Pls type in the student number {n+1}\'s ID: '),input(f'Pls type in the student number {n+1}\'s DoB: ')))

for n in range(class_num):
        print('------------------------------------------')
        holder=classes(input(f'Pls type in the class number {n+1}\'s name: '),input(f'Pls type in the class number {n+1}\'s ID: '),int(int_input(f'Pls type in the class number {n+1}\'s credits: ')))
        List_class.append(holder)
        total_credit+=holder.get_credit()
        for i in List_student: 
            #math 
            List_class[n].grade_input(math.floor(float(int_input(f'Pls type in the {i.get_name()}\'s grade: '))*10)/10)  
            
for n in range(student_num):
    weight=0
    for j in List_class:
        weight+=j.get_grade(n)
    List_student[n].grade_input(weight/total_credit)
        
def main(stdscr):
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_GREEN)
    stdscr.addstr("Sorted Student Information:\n", curses.A_BOLD)
    sorted_student=sorted(List_student,key=lambda sth:-sth.get_grade())
    for student in sorted_student:
        stdscr.addstr(str(student) + "\n", curses.color_pair(1))
    stdscr.addstr("Unsorted Student Information:\n", curses.A_BOLD)
    for student in List_student:
        stdscr.addstr(str(student) + "\n", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getch()
wrapper(main)