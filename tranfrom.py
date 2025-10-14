import math
class Transfrom:
    def __init__(self):
        self.forward = []
        self.inverse = []

    def add_shift(self,n):
        self.forward.append(lambda x: x+n)
        self.inverse.append(lambda x: x-n) 

    def add_scale(self,n):
        self.forward.append(lambda x: x*n)
        self.inverse.append(lambda x: x/n) 

    def add_cantor(self):
        self.forward.append(lambda x: x*(x+1)/2)
        self.inverse.append(lambda x: x - (((math.sqrt(8*x+1))-1/2)*((math.sqrt(8*x+1))-1/2)/2)-1) 

    def full_forward(self,n):
        for f in self.forward:
            n = f(n)
        return n

    def full_inverse(self,n):
        for f in self.inverse:
            n = f(n)
        return n