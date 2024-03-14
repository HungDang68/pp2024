student_num=2
    class_num=2

    List_student.append(student('Hung','BA12-082','12/12/2000'))
    List_student.append(student('Sth','BA12-081','12/12/2003'))
        
            
    List_class.append(classes('Math',1,2))
    List_class.append(classes('English',2,3))

    List_class[0].grade_input(3.4,List_student[0].get_id())
    List_class[0].grade_input(2.4,List_student[1].get_id())
    List_class[1].grade_input(2.4,List_student[1].get_id())
    List_class[1].grade_input(3.4,List_student[0].get_id())

    Grade.append(List_class[0].get_students())
    Grade.append(List_class[1].get_students())
