# Create a sclass programmer for nstoring infomation of feq progrmmer working at microsoft
class Programmer:
    company = 'Microsoft'
    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} is {self.name} and the product is {self.product}")

saurav = Programmer("Saurav", "Skype")
Alka = Programmer("Alka","Github")
saurav.getInfo()
Alka.getInfo()