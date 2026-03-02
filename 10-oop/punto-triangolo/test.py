from punto import Punto
from triangolo import Triangolo

# Test Punto
p1 = Punto(3, 4)
p2 = Punto(3, 4)
p3 = Punto(0, 0)

print(p1)
print("distanza p1-p3:", p1.distanza(p3))  
print("p1 == p2:", p1 == p2)               
print("p1 == p3:", p1 == p3)               

t1 = Triangolo(3, 4, 5)
t2 = Triangolo(3, 4, 5)
t3 = Triangolo(6, 8, 10)
t4 = Triangolo(5, 12, 13)

print("\n", t1)
print("area t1:", t1.area())           
print("perimetro t1:", t1.perimetro()) 
print("t1.equals(t2):", t1.equals(t2)) 
print("t1.equals(t3):", t1.equals(t3)) 
print("t1.equivale(t2):", t1.equivale(t2))
print("t1.equivale(t3):", t1.equivale(t3))
