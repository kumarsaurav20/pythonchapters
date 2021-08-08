# write  __str__ method to print tghe vector as follows
# Answer vector dimension 3 for the problem .


class vector :
    def __init__(self,vec):
        self.vec = vec

    def __str__(self) :
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
        
v1 = vector([1,4,6])
v2 = vector([1,6,5])
print(v1)
print(v2)
        
    