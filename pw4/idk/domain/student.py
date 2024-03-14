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

if __name__=='__main__':
    print({__name__})