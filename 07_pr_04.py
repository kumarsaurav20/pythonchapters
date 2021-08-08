# WAP of recursive function to find the first n natural numbers...

def recur_sum(n):
    if n<=1:
        return n
    else:
        p = recur_sum(n-1) + n
        return p

num = 6 
if num < 0:
    print("Enter a positive number ")
else:
    print("The recursive sum of the number is :", recur_sum(num))