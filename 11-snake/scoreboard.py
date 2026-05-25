from turtle import Turtle


class Panel(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=260)
        self.tally = 0
        self._draw()

    def _draw(self):
        self.clear()
        self.write(f"Score: {self.tally}", align="center", font=("Arial", 24, "normal"))

    def bump(self):
        self.tally += 1
        self._draw()

    def freeze(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Game Over\nScore: {self.tally}", align="center", font=("Arial", 24, "normal"))