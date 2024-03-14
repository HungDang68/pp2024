import sys
sys.path.append(".")
from idk.input import *
from idk import output
from idk.domain.student import *
from idk.domain.classes import *
import math
import curses
from curses import wrapper

# student_num=int(int_input('Please type in a number of students: '))
# print('------------------------------------------')
# class_num=int(int_input('Please type in a number of classes: '))
 
# for n in range(student_num):
#     print('------------------------------------------')
#     List_student.append(student(input(f'Pls type in the student number {n+1}\'s name: '),input(f'Pls type in the student number {n+1}\'s ID: '),input(f'Pls type in the student number {n+1}\'s DoB: ')))

# for n in range(class_num):
#         print('------------------------------------------')
#         holder=classes(input(f'Pls type in the class number {n+1}\'s name: '),input(f'Pls type in the class number {n+1}\'s ID: '),int(int_input(f'Pls type in the class number {n+1}\'s credits: ')))
#         List_class.append(holder)
#         for i in List_student: 
#             #math 
#             List_class[n].grade_input(math.floor(float(int_input(f'Pls type in the {i.get_name()}\'s grade: '))*10)/10)  

student_num=2
class_num=2

List_student.append(student('Hung','BA12-082','12/12/2000'))
List_student.append(student('Sth','BA12-081','12/12/2003'))
    
        
List_class.append(classes('Math',1,2))
List_class.append(classes('English',2,3))

List_class[0].grade_input(3.4)
List_class[0].grade_input(2.4)
List_class[1].grade_input(2.4)
List_class[1].grade_input(3.4)


for int_ in range(class_num):
    total_credit+=List_class[int_].get_credit()

for n in range(student_num):
    weight=0
    for j in List_class:
        weight+=j.get_grade(n)
    List_student[n].grade_input(weight/total_credit)
        

def main (stdscr):
    output.sth(stdscr)

if __name__=='__main__':
  #main('stdscr')
  curses.wrapper(main)