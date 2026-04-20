import turtle as t
import random

a = t.Turtle()
w = t.Screen()

a.speed(0)
t.width(10)

colors = ["red", "green", "blue", "yellow", "purple", "orange", "black"]

while True:
    a.forward(random.choice([50, -50]))
    a.left(random.choice([90,-90]))
    a.color(random.choice(colors))