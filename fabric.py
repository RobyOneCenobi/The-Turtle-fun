import turtle
import random

""" ustawienia początkowe i rysowanie ramki """
pen = turtle.Turtle()
pen.pensize(1)
pen.pencolor('blue')
pen.penup()
pen.goto(-220, 220)
pen.pendown()
pen.forward(400)
pen.right(90)
pen.forward(400)
pen.right(90)
pen.forward(400)
pen.right(90)
pen.forward(400)
pen.penup()
pen.goto(-200, 200)
pen.pendown()
pen.right(90)


""" losowanie czy kawadrat bedzie pusty czy pełny """
def sygnal():
    sygnal = random.randint(1, 2)
    return sygnal


""" rysowanie kwadratu pustego """
def kwadrat_pusty():
    pen.pendown()
    pen.left(180)
    for i in range(0, 3):
        pen.forward(20)
        pen.right(90)
    pen.forward(20)
    pen.left(90)
    return kwadrat_pusty


""" rysowanie kwadratu pełnego """
def kwadrat_pelny():
    pen.down()
    pen.left(180)
    pen.begin_fill()
    for i in range(0, 3):
        pen.forward(20)
        pen.right(90)
    pen.forward(20)
    pen.end_fill()
    pen.left(90)
    return kwadrat_pelny


""" rysowanie kwadratu pełnego lub pustego """
def rysuj_kwadrat(sygnal):
    if sygnal == 1:
        kwadrat_pelny()
        pen.penup()
        pen.forward(20)
    else:
        kwadrat_pusty()
        pen.penup()
        pen.forward(20)


""" przesuwanie sie do kolejnej linii """
def w_dol(ile_razy):
    pen.goto(-200, 200 - 20*ile_razy)
    return w_dol


""" rysowanie wzoru na formatce 20x20 """
ile_razy = 1
while ile_razy <=20:
    for w in range(0, 20):
        sygnal( )
        s = sygnal( )
        rysuj_kwadrat(s)
    w_dol(ile_razy)
    ile_razy += 1

turtle.mainloop()
