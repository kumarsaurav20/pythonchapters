# Can you change the self parameter inside a class to something else (say,'Saurav')
# try changing 'slf' or 'saurav' and see the effects ::
class sample():
    def __init__(slf,name):
        slf.name = name

obj = sample("Saurav")
print(obj.name)


        