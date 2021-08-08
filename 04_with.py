# Use of with command
with open('another.txt','r') as f:
    a = f.read()

with open('another.txt','w') as f:
    a = f.write("Hii i am Saurav")
print(a)
