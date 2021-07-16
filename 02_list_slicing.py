
# We can create list with item of differen types
from typing import ForwardRef


c = [45, "Saurav",24.56 ,False]
print(c)
print(type(c))

'''on using print(type(c)) it will show that <class list>'''

# List slicing
freinds = ["Saurav","Rahul","Lalit","Ratan","Priya"]
print(freinds[0:4])
print(freinds[0:2])
print(freinds[-4:-1])

# Changing values in list 
freinds[0:1] = ["Vishal","Aman"]
print(freinds)