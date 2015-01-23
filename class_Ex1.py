#Kieran Burnett
#23-01-2015
#records class_Ex1

class student_info:
    def __init__(student):
        student.name = None
        student.marks = None

def student_list():
    temp = int(input("Please enter the ammount of students being entered: "))
    student_records = []
    for count in range(temp):
        student = student_info()
        student.name = input("Please enter the students name: ")
        student.marks = int(input("Please enter their marks: "))
        student_records.append(student)
    return student_records

def display():
    for count in range(len(student_records)):
        print(student_records[count].name,"With a score of",student_records[count].marks)
                            
student_records = student_list()
display()
