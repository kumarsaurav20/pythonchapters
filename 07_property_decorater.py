class Employee:
    company = "Google"
    salary = 4500
    salarybonus= 500

    @property
    def totalsalary(self):
        s = (self.salary + self.salarybonus)
        return s
        #or we can use 
        # return self.salarybonus+self.salary
    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus= val-self.salary

e = Employee()
print(e.totalsalary)
e.totalsalary = 5000  #if we want to change the value of totalsalary
print(e.salary)
print(e.salarybonus)

