# WAP to find the sum of first natural number using while loop ::
num = int(input("Enter the number\n:"))
if num<=0:
    print("Enter the positive number:")
else:
    sum = 0
    while(num>0):
        sum+=num
        num-=1
        print("The sum is",sum)
