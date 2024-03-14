List_student=[]
List_class=[]
total_credit=0
student_num=0
class_num=0
sorted_student=[]

def int_input(string):
    while(True):
      try:
        n=float(input(f'{string}'))
        return n
      except Exception as x:
            print("Try again")

if __name__=='__main__':
    print({__name__})