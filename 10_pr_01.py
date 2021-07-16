# WAP to print multiplication table of a given number using for loop
table =int(input("Enter the number of table\n"))
for i in range (1, 11):
    
    print(str(table)+ "X"+str(i)+"="+str(i*table))
    
    print(f"{table}x{i}={table*i}")

    ''' This is f strings  '''