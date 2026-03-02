import math

class Triangolo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def setA(self, a):
        self.a = a
    
    def setB(self, b): 
        self.b = b
        
    def setC(self, c):
        self.c = c
        
    def getA(self):
        return self.a
    
    def getB(self):
        return self.b
    
    def getC(self):
        return self.c
    
    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimetro(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"Triangolo({self.a}, {self.b}, {self.c})"

    def equals(self, t):
        return self.a == t.a and self.b == t.b and self.c == t.c

    def equivale(self, t):
        return self.area() == t.area()
