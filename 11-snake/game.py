from turtle import Screen
from snake import Kappa
from food import Nib
from scoreboard import Panel
import time

stage = Screen()
stage.setup(600, 600)
stage.bgcolor("black")
stage.title("Snake")
stage.tracer(0)

runner = Kappa()
bait = Nib()
hud = Panel()

stage.listen()
stage.onkey(runner.turn_n, "Up")
stage.onkey(runner.turn_s, "Down")
stage.onkey(runner.turn_w, "Left")
stage.onkey(runner.turn_e, "Right")

alive = True
while alive:
    stage.update()
    time.sleep(0.1)
    runner.drift()

    if runner.tip.distance(bait) < 15:
        bait.hop()
        hud.bump()
        runner.stretch()

    if runner.tip.xcor() > 280 or runner.tip.xcor() < -280 or runner.tip.ycor() > 280 or runner.tip.ycor() < -280:
        alive = False

    for unit in runner.chain[1:]:
        if runner.tip.distance(unit) < 10:
            alive = False

hud.freeze()
stage.update()
stage.exitonclick()