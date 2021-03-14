# Define classes and objects in Python. Create a class called Employee and initialize it
# with employee id and name. Design methods to:
# (i) setAge_to assign age to employee.
# (ii) setSalary_to assign salary to the employee.
# (iii) Display_to display all information of the employee.

class Employee:
    def __init__(self, empID, empName):
        self.empID = empID
        self.empName = empName

    def setAge(self, empAge):
        self.empAge = empAge

    def setSalary(self, empSal):
        self.empSal = empSal

    def display(self):
        print('\nEmployee Details: ')
        print(
            f'ID: {self.empID}\nName: {self.empName}\nAge: {self.empAge}\nSalary: {self.empSal}')


a = Employee(
    input('Enter the Employee ID: '), input('Enter the Employee Name: '))
a.setAge(input('Enter the Employee Age: '))
a.setSalary(input('Enter the Employee Salary: '))
a.display()
