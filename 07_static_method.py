
class Employee:
    company = "Google"

    def getSalary(self,):
        print(f"Salary for this employee working is {self.company} is {self.salary}")
    
    @staticmethod
    def greet ():
        print("Good morning, sir")

saurav = Employee()
saurav.salary = 10000
saurav.getSalary()

saurav.greet()
# Employee.getSalary(saurav)
