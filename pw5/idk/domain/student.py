from dataclasses import dataclass, field

@dataclass
class student():   
    __students: str
    __id: str
    __Dob: str
    __gpa: float= field(init=False)
        
    def get_name(self):
        return self.__students
    
    def grade_input(self,grade):
        self.__gpa=grade
        
    def get_grade(self):
        return self.__gpa
    
    def __str__(self) -> str:
        return f"Name: {self.__students}  ID: {self.__id}  DOB: {self.__Dob}  GPA: {self.__gpa}"
    
    def get_id(self):
        return self.__id