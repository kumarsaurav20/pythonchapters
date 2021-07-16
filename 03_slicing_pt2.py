# This is slicing part 2

name = "Saurav"
print(name[5])
# Here we are using length-1 
# Thats why we enter [5] in braces.
# After entering 5 in braces It will show the 5th character as output
# If we will use [6] in braces it will show error 
# Beacause in programming language we start
# counting from 0 :::::: 

# If we want to print character from 0 to 3 or 0 to 4 
# or 1 to 3 , 2 to 4 e.t.c
# We use print(name[0:4])

print(name[0:4]) 
# we can aslo use print(name[:4]) this will not give any error
 #print(name[0:]) Also this is same but it will give full value "Saurav"
# print(name[1:]) This will give value "Aurav" S will not include as i use [1:] in braces

'''As we can see in output it is giving (Saur) 
   Which is correct value
   *** Here we learn how to use slicing  '''
