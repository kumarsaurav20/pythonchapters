# Use of files ...

f = open('sample.txt','r') # open the file in read mode 
# data = f.read() Read it's content 
data = f.read(6) #Reads first five char. from txt file 

print(data) #Print the content 
f.close()#close the file 

