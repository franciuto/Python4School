import turtle as t
import random

a = t.Turtle()
w = t.Screen()
w.colormode(255)

a.speed(0)
t.width(10)

def random_rgb():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

i = 0
while True:
    i += 1
    a.circle(100)
    a.right(i)
    a.color(random_rgb())