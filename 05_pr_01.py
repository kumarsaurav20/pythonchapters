# WAP to find greatest of four numbers entered by the user

n1 = int(input("Enter the number 1\n"))
n2 = int(input("Enter the number 2\n"))
n3 = int(input("Enter the number 3\n"))
n4 = int(input("Enter the number 4 \n"))

if(n1>n4):
   f1 = n1
else:
    f1 = n4
if(n2>n3):
   f2 = n2
else:
    f2 = n3
if(f1>f2):
    print(str(f1) + "is greatest")
else:
    print(str(f2) + "is greatest")