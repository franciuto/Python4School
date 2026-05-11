import turtle as t


PASSO = 15

schermo = t.Screen()
schermo.title("Lavagnetta magnetica")
schermo.bgcolor("#f2f2f2")
schermo.setup(width=700, height=500)

penna = t.Turtle()
penna.shape("circle")
penna.shapesize(0.6, 0.6)
penna.color("#202020")
penna.pensize(3)
penna.speed(0)

sta_disegnando = True


def su():
    penna.setheading(90)
    penna.forward(PASSO)


def giu():
    penna.setheading(270)
    penna.forward(PASSO)


def sinistra():
    penna.setheading(180)
    penna.forward(PASSO)


def destra():
    penna.setheading(0)
    penna.forward(PASSO)


def pulisci():
    penna.clear()
    penna.penup()
    penna.home()
    if sta_disegnando:
        penna.pendown()


def toggle_penna():
    global sta_disegnando
    sta_disegnando = not sta_disegnando
    if sta_disegnando:
        penna.pendown()
    else:
        penna.penup()


schermo.listen()
schermo.onkey(su, "Up")
schermo.onkey(giu, "Down")
schermo.onkey(sinistra, "Left")
schermo.onkey(destra, "Right")
schermo.onkey(pulisci, "c")
schermo.onkey(toggle_penna, "space")

schermo.exitonclick()
