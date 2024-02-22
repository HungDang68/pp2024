import numpy as np

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