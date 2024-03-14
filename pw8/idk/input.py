List_student=[]
List_class=[]
total_cre=0
student_num=0
class_num=0
Grade=list()
List_file:list=[]
sorted_student:list


def int_input(string)-> float:
    while(True):
      try:
        n=float(input(f'{string}'))
        return n
      except Exception as x:
            print("Try again")


def sort_student()->None:
  global sorted_student
  sorted_student=sorted(List_student,key=lambda sth:-sth.get_grade())





if __name__ =="__main__":
    print('hi')