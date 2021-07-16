# WAp to find ou whether a student is pass or fail,
# if it requires total 40% and 35% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.
 
s1 = int(input("Enter the marks of first subject\n "))
s2 = int(input("Enter the marks of second subject\n"))
s3 = int(input("Enter the marks of third subject\n"))

if(s1<33 or s2<33 or s3<33):
    print("you are fail")
elif(s1+s2+s3)/3 <40:
    print("You are pass")
else:
    print("Congratulations! You passed the exam")
