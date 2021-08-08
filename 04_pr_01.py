# WAP using function to find the greatest of three number.
def maximum(n1,n2,n3):
    if (n1>n2):
        if(n1>n3):
          return n1
        else:
            return n3
    else:
         if(n2>n3):
            return n2
         else:
             return n3

m = maximum(11,55,20)
print("The value of the maximum " + str(m))

