class  Employee:
    company = "Google"
    salary = 100

saurav = Employee()
vishal = Employee()

# Creating instance attribute salary for both the objects
# saurav.salary = 300
# vishal.salary = 400
print(saurav.company)
print(vishal.company)
Employee.company = "Youtube"
print(saurav.company)
print(vishal.company)
print(vishal.salary)
print(vishal.salary)

# print(saurav.adress)
# Above syntax will throw an error as address is not present in instance/class  
