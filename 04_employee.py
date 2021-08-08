class  Employee:
    company = "Google"
    salary = 100
    '''salary and company is attribuute of class'''

saurav = Employee()
vishal = Employee()
saurav.salary = 300
vishal.salary = 400
print(saurav.company)
print(vishal.company)
Employee.company = "Youtube"
print(saurav.company)
print(vishal.company)
print(vishal.salary)
print(vishal.salary)
