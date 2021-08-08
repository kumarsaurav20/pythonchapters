class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working is {self.company} is {self.salary}")

saurav = Employee()
saurav.salary = 10000
saurav.getSalary()
# Employee.getSalary(saurav)
