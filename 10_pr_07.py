# WAP a python function to print multiplication table of a given number::
def table(n):
    for i in range(1,11):
        print("%d * %d = %d" % (n,i, n*i))
n = int(input("Enter the number: \n"))
print("Done ", table(n))
