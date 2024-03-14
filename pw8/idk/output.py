import curses
#from .input import List_student
#from .input import sorted_student
from .domain.classes import *
import pickle
import lzma

def sth(stdscr):
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_GREEN)
    
    
    stdscr.addstr("Student Information:\n", curses.A_BOLD)
    with open("students.txt",'rb') as f:
        holder_student=pickle.load(f)
    for student in holder_student:
        stdscr.addstr(str(student) + "\n", curses.color_pair(1))
    
    stdscr.addstr("Sorted Student Information:\n", curses.A_BOLD)
    with open("sorted.txt",'rb') as f:
        holder_sorted_student=pickle.load(f)
    for sorted in holder_sorted_student:
        stdscr.addstr(str(sorted) + "\n", curses.color_pair(1))
    
    stdscr.addstr("Classes Information:\n", curses.A_BOLD)
    with open("courses.txt",'rb') as f:
        holder_class=pickle.load(f)
    for clas in holder_class:
        stdscr.addstr(str(clas) + "\n", curses.color_pair(1))
    
    
    stdscr.addstr("Grades Information:\n", curses.A_BOLD)
    with open("marks.txt",'rb') as f:
        holder_grade=pickle.load(f)
    for marks in range(len(holder_grade)):
        stdscr.addstr(f"{holder_class[marks].get_name()}\n", curses.A_BOLD)
        stdscr.addstr(f'{holder_grade[marks]}\n', curses.color_pair(1))
    
    
    stdscr.refresh()
    stdscr.getch()

if __name__ =="__main__":
    print('hi')
