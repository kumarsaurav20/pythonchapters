## adding value to an empty set
b = set()
print(type(b))

b.add(4)
b.add(5)

b.add(5) #As we knw that sets is a collection of non-repetative elements
# In out put there will be only one 5 

b.add(7)

# b.add([4, 5, 6]) On adding this will show error 
''' Try to add list in a set'''
# As we knw list is not hashable in a set

b.add((4,5,6)) #By this way we can add value in set
print(b)


# We cannot add list and dictonary in set
 
##Print lenght of set
print(len(b)) 

## Removable of an item
b.remove(4)
print(b)

b.pop() #Removes an arbitrary element from set
print(b)

b.clear()#Empties the set 
print(b)

b.union({8,11}) #Returns a new set
print(b)