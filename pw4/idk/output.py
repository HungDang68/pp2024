import numpy as np
import curses
from .input import List_student
from .input import sorted_student

def sth(stdscr):
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


