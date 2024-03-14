import threading
import time
import sys
sys.path.append(".")
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

def sth(int_:int):
    print('hi')
    time.sleep(int_)
    print('bye')

print('no hi')
if __name__ == '__main__':
    t3 = threading.Thread(target=pickle.dump, args=(List_student,open('students.txt','wb')))
    t2 = threading.Thread(target=sth, args=(2,))
    t1 = threading.Thread(target=sth, args=(1,))
    t1.start()
    t2.start()
    # t1.join()
    t2.join()

print('no hi')
    