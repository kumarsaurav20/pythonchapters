# Inheritance:::
class Employee :
    company = 'Microsoft'

    def showdetail(self):
        print(f"This is an employee")

class Programmer(Employee):
    language = 'Python'
    def getName(self):
        print(f"The language{self.language}")

    def showdetail(self):
        print("This is an Programmer")


e = Employee()
e.showdetail()
p = Programmer()
p.showdetail()
