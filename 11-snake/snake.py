from turtle import Turtle

_STEP = 20
_STARTS = [(0, 0), (-20, 0), (-40, 0)]
_UP = 90
_DOWN = 270
_LEFT = 180
_RIGHT = 0


class Kappa:
    def __init__(self):
        self.chain = []
        self._seed()
        self.tip = self.chain[0]

    def _seed(self):
        for spot in _STARTS:
            self._add(spot)

    def _add(self, pos):
        unit = Turtle("square")
        unit.color("white")
        unit.penup()
        unit.goto(pos)
        self.chain.append(unit)

    def stretch(self):
        self._add(self.chain[-1].position())

    def drift(self):
        for idx in range(len(self.chain) - 1, 0, -1):
            nx = self.chain[idx - 1].xcor()
            ny = self.chain[idx - 1].ycor()
            self.chain[idx].goto(nx, ny)

        self.tip.forward(_STEP)

    def turn_n(self):
        if self.tip.heading() != _DOWN:
            self.tip.setheading(_UP)

    def turn_s(self):
        if self.tip.heading() != _UP:
            self.tip.setheading(_DOWN)

    def turn_w(self):
        if self.tip.heading() != _RIGHT:
            self.tip.setheading(_LEFT)

    def turn_e(self):
        if self.tip.heading() != _LEFT:
            self.tip.setheading(_RIGHT)