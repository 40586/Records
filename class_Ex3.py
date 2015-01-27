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

def display(employee_records):
    for count in range(len(employee_records)):
        print("*" * 40)
        print("* Pay Slip"," " *27,"*")
        print("* Name: {0} {1:>{2}}".format(employee_records[count].name,"*",31-(len(str(employee_records[count].name)))))
        print("* Employee Number: {0} {1:>{2}}".format(employee_records[count].number,"*",20-(len(str(employee_records[count].number)))))
        print("* Hours Worked: {0} {1:>{2}}".format(employee_records[count].hours,"*",23-(len(str(employee_records[count].hours)))))
        print("* Rate of pay: {0} {1:>{2}}".format(employee_records[count].pay_rate,"*",24-(len(str(employee_records[count].pay_rate)))))
        print("*"," "*36,"*")
        total = employee_records[count].hours*employee_records[count].pay_rate
        print("* Total pay: {0} {1:>{2}}".format(total,"*",26-(len(str(total)))))
        print("*" * 40)

employee_records = employee_list()
display(employee_records)
