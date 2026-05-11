from turtle import Turtle, Screen
import time

class Snake():
    def __init__(self):
        self.segments = self.initializeSegments()
    
    def initializeSegments(self):
        positions = [(0,0), (-20,0), (-40,0)]
        segments = []
        
        for position in positions:
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(position)
            segments.append(turtle)
        return segments

    def move(self):    
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.segments[0].forward(20)