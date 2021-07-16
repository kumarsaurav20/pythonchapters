# WAP to fill in a letter tempelate given below with name and date

letter = '''Dear <|Name|> 
You are selected ! 

Date: <|Date|>'''
name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)