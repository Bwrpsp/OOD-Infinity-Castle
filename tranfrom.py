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

    def full_forward(self,n):
        for f in self.forward:
            n = f(n)
        return int(round(n))

    def full_inverse(self,n):
        for f in reversed(self.inverse):
            n = f(n)
        return n
    def reset(self):
        self.forward = []
        self.inverse = []