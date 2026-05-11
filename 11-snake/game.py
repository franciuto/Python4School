from turtle import Screen
from snake import Snake 
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake final")
screen.tracer(0)

snake = Snake()

live = True
while live:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()