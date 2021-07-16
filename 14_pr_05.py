# WAP to calculate the factorial of a given number using for loop :::
num = int(input("Enter the number\n:"))
for i in range (1 , num+1): 
    factorial = 1
    for i in range(1 , num+1):
        factorial = factorial + 1
        print(f"The factorial of {num} is {factorial}")
