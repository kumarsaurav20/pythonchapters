myDict = {
"name" : "saurav",
"work" : "coder",
"marks" : [1, 2, 3, 4]

}
# Printing method of keys in a dictionary
print(myDict.keys())
print(type(myDict.keys()))
print(list(myDict.keys()))

# Printing method of values in a dictionary
print(myDict.values())
print(type(myDict.values()))
print(list(myDict.values()))

# To print all the items (Keys, values) in a dictonary
print(myDict.items())

updateDict = {
    "ratan": "freind",
    "ajeet": "freind"
}
myDict.update(updateDict) #updae the dict. by adding key-value pairs from updateDict
print(myDict)

print(myDict.get["name2"]) #throws no error whether given key is present in dict or not
print(myDict["name2"]) #throws an error as name2 is not present in the dict.

'''We can see the main difference between two syntax which can give same value if key is present'''
