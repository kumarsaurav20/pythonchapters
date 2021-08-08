# Write a class train which has methods to book a ticket ,
# get status and get fare info. of trains running under Indian Railway.
class Train :
    def __init__(self,name,fare, seats) :
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print("*************")
        print(f"The name of the train is {self.name}")
        print(f"The train seats available in the train are {self.seats}")
        print("**************")

    def fareInfo(self):
        print(f"The price of the ticket is : Rs{self.fare}")

    def booksTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! your seat number is {self.seats} ")
            self.seats = self.seats-1
        else:
            print("Sorry seats is not available . Try for Tatkal")

intercity = Train("Intercity Express:20310",90,100)
intercity.getStatus()
intercity.booksTicket()
intercity.booksTicket()
intercity.getStatus()


        