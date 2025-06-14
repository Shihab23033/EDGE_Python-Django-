import cmath
class ImgCalc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Calc(self,op):
        if op == '+':
            return self.a + self.b
        elif(op == '-'):
            return self.a - self.b
        elif(op=='/'):
            return self.a / self.b
        elif(op=='*'):
            return self.a * self.b
        
        