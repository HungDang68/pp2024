List_student=[]
List_class=[]
total_cre=0
student_num=0
class_num=0
Grade=list()
List_file:list=[]

def int_input(string)-> float:
    while(True):
      try:
        n=float(input(f'{string}'))
        return n
      except Exception as x:
            print("Try again")


def sort_student()->list:
  sorted_student=sorted(List_student,key=lambda sth:-sth.get_grade())
  return sorted_student




if __name__ =="__main__":
    print('hi')