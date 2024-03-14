import numpy as np
from dataclasses import dataclass, field

@dataclass
class classes():
    __couse: str            
    __id: str
    __credit: int
    __students: dict = field(default_factory=dict)
     
    def grade_input(self,grade,id):
        self.__students.update({id:grade}) 
    
    def get_credit(self):
        return self.__credit
    
    def get_name(self):
        return self.__couse
    
    def get_grade(self,id:str):
        return self.__students[id]*self.__credit
    
    def get_id(self):
        return self.__id
    
    def get_students(self):
        return self.__students
    
    def __str__(self) -> str:
        return f"Course: {self.__couse}   ID: {self.__id}   Credit: {self.__credit}"