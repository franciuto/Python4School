import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distanza(self, punto):
        return math.sqrt(pow((self.x - punto.x), 2) + pow((self.y - punto.y), 2))
    
    def __eq__(self, punto):
        return self.x == punto.x and self.y == punto.y 
    
    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def __str__(self):
        return f'Il punto ha coordinate {self.x}, {self.y}'