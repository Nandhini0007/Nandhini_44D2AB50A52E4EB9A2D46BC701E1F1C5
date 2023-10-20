
def __init__(self,                   name, roll_number, cpga):
    self.name=name
    self.roll_number=roll_number
    self. cpga=cpga
def sort_students(student_list):
sorted_students=sorted(student_list, key=lambda student:                student.cpga, reverse=true)
    return  sorted_students
students=                              [student("anitha",                "A123",7.8),student("           kalaiselvi","A124",8.9,student("srimathi","A125",9.1)student("Tamil","A126",9.9)]
sorted_students=sort_student(students)
for student in sorted_students:
  print("Name:{}, Roll number:    {}, CGPA:                         {}". format(student. name, student. roll_number, student. cpga))