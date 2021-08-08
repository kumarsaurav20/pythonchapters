# Write a python function which converts inches to cm:::
def inch_cm(n):
    cm = float(n*2.54) 
    return cm
n= float(input("Enter the value in inch:"))

print("The value in cm is:", inch_cm(n))
