class Employee:
    company ="Linc"
    salary = 100
    location = "delhi"

    # def changesalary(self, sal):
    #    self.__class___.salary = sal

    @classmethod  #As we are not using self parameter here That's why we are using class method...
    
    def changesalary(cls,sal):
        cls.salary= sal

e = Employee()
print(e.salary)
e.changesalary(455)
print(e.salary)
print(Employee.salary)
