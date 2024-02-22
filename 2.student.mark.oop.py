class classes():
    def __init__(self,n,i):
       self.__couse=n
       self.__id=i
       self.__students= list()
    
    def grade_input(self,grade):
        self.__students.append(grade)
    
    def __str__(self):
        return f"Name: {self.__couse}  "
    
    def get_grade(self,num):
        return f"{self.__students[num]}"
    
    def get_credit(self):
        return self.__credit

    
class student:  
    def __init__(self,n,i,dob):
        self.__students=n
        self.__id=i
        self.__Dob=dob
    
    def __str__(self):
        return f'Name: {self.__students} ID: {self.__id} DoB: {self.__Dob}'
        
    def get_name(self):
        return self.__students
    
    def grade_input(self,grade):
        self.__gpa=grade
        
    def get_grade(self):
        return self.__gpa
    
List_student=[]
List_class=[]
student_num=0
class_num=0

def int_input(string):
    while(True):
      try:
        n=float(input(f'{string}'))
        return n
      except Exception as x:
            print("Try again")


student_num=int(int_input('Please type in a number of students: '))
print('------------------------------------------')
class_num=int(int_input('Please type in a number of classes: '))
 
for n in range(student_num):
    print('------------------------------------------')
    List_student.append(student(input(f'Pls type in the student number {n+1}\'s name: '),input(f'Pls type in the student number {n+1}\'s ID: '),input(f'Pls type in the student number {n+1}\'s DoB: ')))

for n in range(class_num):
        print('------------------------------------------')
        holder=classes(input(f'Pls type in the class number {n+1}\'s name: '),input(f'Pls type in the class number {n+1}\'s ID: '))
        List_class.append(holder)
        for i in List_student: 
            List_class[n].grade_input((float(int_input(f'Pls type in the {i.get_name()}\'s grade: '))))  


for x in List_student:
    print(x)
    
    
for x in List_class:
    print(x)
    for n in range(class_num):
        print(f'{List_student[n].get_name()}: {x.get_grade(n)}')



