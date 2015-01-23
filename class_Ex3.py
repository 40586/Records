#Kieran Burnett
#23-01-15
#Class_Ex3

class employee_info:
    def __init__(er):
        er.name = None
        er.number = None
        er.hours = None
        er.pay_rate = None

def employee_list():
    temp = int(input("Please enter the ammount of employees being entered: "))
    employee_records = []
    for count in range(temp):
        employee = employee_info()
        employee.name = input("Please enter the employee's name: ")
        employee.number = int(input("Please enter their number: "))
        employee.hours = int(input("Please enter their hours: "))
        employee.pay_rate = int(input("Please enter their hourly rate of pay: "))
        employee_records.append(employee)
    return employee_records

def display():
    for count in range(len(employee_records)):
        print("*" * 20)
        print("* Pay Slip"," " *9,"*")
        print
