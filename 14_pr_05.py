
class vector :
    def __init__(self,vec):
        self.vec = vec

    def __str__(self) :
        str1 = ""
        indedx = 0 
        for i in self.vec:
            str1 += f"{i}a{indedx} +"
            indedx +=  1 
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i]+ vec2.vec[i])

        return vector(newList)

v1 = vector([1,4,6])
v2 = vector([1,6,5])
print(v1 + v2)
        
    