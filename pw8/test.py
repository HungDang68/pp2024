import sys
sys.path.append(".")
import threading
import time
from idk.input import *
from idk import output
from idk.domain.student import *
from idk.domain.classes import *
import math
import curses
from curses import wrapper
import pickle
from zipfile import ZipFile
import os


path = './students.dat'
check=os.path.exists(path)
if check==True:
    with ZipFile('students.dat','r')as myzip:
     myzip.extractall()
             
else:
    # ##Input number of student and classes 
    # student_num=int(int_input('Please type in a number of students: '))
    # print('------------------------------------------')
    # class_num=int(int_input('Please type in a number of classes: '))

    # ##Student input
    # for n in range(student_num):
    #     print('------------------------------------------')
    #     holder=student(input(f'Pls type in the student number {n+1}\'s name: '),input(f'Pls type in the student number {n+1}\'s ID: '),input(f'Pls type in the student number {n+1}\'s DoB: '))
    #     List_student.append(holder)

    # ##Class input
    # for n in range(class_num):
    #         print('------------------------------------------')
    #         holder=classes(input(f'Pls type in the class number {n+1}\'s name: '),input(f'Pls type in the class number {n+1}\'s ID: '),int(int_input(f'Pls type in the class number {n+1}\'s credits: ')))
    #         List_class.append(holder)
    #         for i in range(len(List_student)): 
    #             #math//grade input
    #             List_class[n].grade_input(math.floor(float(int_input(f'Pls type in the {List_student[i].get_name()}\'s grade: '))*10)/10,List_student[i].get_id())
    #         Grade.append(List_class[n].get_students())
    
    
    
    student_num=2
    class_num=2

    List_student.append(student('Hung','BA12-082','12/12/2000'))
    List_student.append(student('Sth','BA12-081','12/12/2003'))
        
            
    List_class.append(classes('Math',1,2))
    List_class.append(classes('English',2,3))

    List_class[0].grade_input(3.4,List_student[0].get_id())
    List_class[0].grade_input(2.4,List_student[1].get_id())
    List_class[1].grade_input(2.4,List_student[1].get_id())
    List_class[1].grade_input(3.4,List_student[0].get_id())

    Grade.append(List_class[0].get_students())
    Grade.append(List_class[1].get_students())




    for int_ in range(class_num):
       total_cre+=List_class[int_].get_credit()

    for n in range(student_num):
      weight=0
      for j in List_class:
        weight+=j.get_grade(List_student[n].get_id())
      List_student[n].grade_input(weight/total_cre)
    
    
    
    pickle.dump(List_student,open('students.txt','wb'))
    pickle.dump(List_class,open('courses.txt','wb'))
    pickle.dump(Grade,open('marks.txt','wb'))

    with ZipFile('students.dat','w')as input_:
        input_.write('students.txt')
        input_.write('courses.txt')
        input_.write('marks.txt')



def main(stdscr):
    output.sth(stdscr)


if __name__=='__main__':
  curses.wrapper(main)