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
        super().takebreath()
        print("I am a programmer so i am breathtaking ***...")



p = Person()
p.takebreath()
e = Employee()
e.takebreath()
print(e.company)
pr = Programmer()
pr.takebreath()
print(pr.company)
print(p.country)


