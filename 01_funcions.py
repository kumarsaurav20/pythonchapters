# Use of function
# Example
# marks1 = [45, 60, 70, 77]
# precentage1 = (sum(marks1)/400)*100

# marks2 = [60,70,75,80]
# percentage2 =((marks2[0] + marks2[1]+ marks2[2]+ marks2[3])/400)*100
# print(precentage1 , percentage2 )

'''We can use sum to short the line of code and make it easy
*** Here sum used as a function to add the marks in the list
**** By this way it makes code lenghty'''
# Now we will use one more way to find percentage.
def percent(marks):
    p =((marks[0] + marks[1]+ marks[2]+ marks[3])/400)*100
    return p  

marks3 = [45, 60, 70, 77]
percentage3 = percent(marks3)

marks4 = [60,70,75,80]
precentage4 = percent(marks4)
print(percentage3,precentage4)
