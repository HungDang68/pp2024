def couseup(couse:dict,student:str,grade:float):
    couse[student]=grade

studentnum=int(input("Please type in a number of students: "))
students=[]

for i in range(studentnum):
    students.append(input('Pls type in the student name: '))
    globals()[students[i]]={'id':input(f'id({students[i]}) pls: '),
                            'name':students[i],
                            'dob':input(f'Dob({students[i]}) pls: ')}

cousenum=int(input("Please type in a number of couses:"))
couses=[]

for i in range(cousenum):
    couses.append(input('Pls type in the couse: '))
    globals()[couses[i]]={'id':input(f'id({couses[i]}) pls: '),
                          'name':couses[i]}

print(f"{couses}")
n=int(input("pick one to update the grade of(1 or 2....) "))

for i in range(studentnum):
    couseup(globals()[couses[n-1]],students[i],float(input(f"Pls input the student {students[i]}s grade: "))) 

print(couses)
print(students)
print(globals()[couses[n-1]])