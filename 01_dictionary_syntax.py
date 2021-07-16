from typing import Dict

myDict = {
"Name" : "Saurav",
"Work" : "coder",
"Marks" : [1, 2, 3, 4]

}
#Here name is a key and Saurav is a value and so on others  
# We will use below syntax to print the value of mydict

print(myDict['Name'])
print(myDict['Work'])
print(myDict['Marks'])

myDict = {
"Name" : "Saurav",
"Work" : "coder",
"Marks" : [1, 2, 3, 4] ,
"anotherdict": {'saurav': 'Player'}

# We can other dictionary in my dict by using This syntax given just above the comment

}

print(myDict['anotherdict']['saurav'])
# To print the value of added dictionary we use syntax like this in given syntax
