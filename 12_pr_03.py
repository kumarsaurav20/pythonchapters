# WAP to find whether a given number is prime or not:::
p = int(input("Enter the number\n"))
prime = True
for i in range(2 ,p):
    if(p%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else :
    print("This number is not prime")
