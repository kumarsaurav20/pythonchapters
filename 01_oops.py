# Use of object oreiented [prog]
class Myself():
    def __init__(self,name,address,qualification):
        self.name = name
        self.address = address
        self.qualification = qualification
    def getInfo(self):
        print(f" My name is {self.name}.\n I am from {self.address}.\n I have completed my graduation degree in {self.qualification}. ")
       

Saurav = Myself("Saurav","Bihar","BCA")
Saurav.getInfo()



