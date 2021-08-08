# WAP to read the text from a given file poems.txt and  find out whether it combines the word twinkle 
f = open('poem.txt')
t = f.read()
if 'Twinkle' in t:
    print("Twinkle is present ")
else:
    print("Twinkle is not present")

f.close()

