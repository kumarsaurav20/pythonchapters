# To calculate the number of character in a sentence 
from typing import Counter


about = "I am a beginner in python programming and iam learning online with the help of Youtube"
print(len(about))
# IT will calculate the character in(About)

print(about.endswith("notes"))
# This will give value in True or False

print(about.count("a"))
# This will tell how many times char(a) is used in given sentence in about
# Ww can also count for multiple char and strings.

print(about.capitalize())
# This will capitalize the first letter.
print(about.find("python"))
# This will tell about first occurance of this word
print(about.replace("python","c++"))
# This will replace the oldword into newword


