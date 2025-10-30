class Employee:
    def __init__(self, name):
        self.__name = name
        self.__salary = 0.0
    def set_salary(self, amount):
        if amount > 0:
            self.__salary =  amount
        else:
            print("invalid salary")
    def get_salary(self):
        return self.__salary
    def get_name(self):
        return self.__name
name = input("enter employee name: ")
emp = Employee(name)
salary = float(input("enter the salary amount: "))
emp.set_salary(salary)
print("Employee name:", emp.get_name( ))
print("Employee Salary:", emp.get_salary ( ))
