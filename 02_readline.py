# Read line command

f = open('sample.txt','r')  

# Read the first line 
data = f.readline()
print(data)

# Read the second line 
data = f.readline()
print(data)
f.close()#close the file 

