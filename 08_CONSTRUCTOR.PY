
class Employee:
    company = "Google"

    def __init__(self,name ,salary, subunit): #Constructor is created
        self.name= name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self,signature):
        print(f"Salary for this employee working is {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def greet ():
        print("Good morning, sir")

saurav = Employee("Saurav",100,"YouTube")
saurav.getDetails()
# Employee.getSalary(saurav)
