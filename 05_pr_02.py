# WAP to convert celcius into Farhneit ::

def farh(cel):
    p = (cel*(9/5)) + 32
    return p

c = 30
f = farh(c)
print("Fahrenite Temperature is " + str(f))