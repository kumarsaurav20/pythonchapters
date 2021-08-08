class Person:
    country = "India"
    def takebreath(self):
        print("I am breathing....")

class Employee :
    company = "Honda"

    def getsalary(self):
        print(f"Salary is {self.salary}")


    def takebreath(self):
        print("I am an Employee so i am luckily breathing ..")

class Programmer(Employee):
    company = "Fiverr"

    def getsalary(self):
        print(f"No salary to Programmers")

    def takebreath(self):
        print("I am Breathing>>>>")


p = Person()
p.takebreath()
e = Employee()
e.takebreath()
print(e.company)
pr = Programmer()
print(pr.company)
print(p.country)
pr.takebreath()


