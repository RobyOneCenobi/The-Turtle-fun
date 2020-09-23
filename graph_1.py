import turtle as tr
import time


pen = tr.Turtle()
tr.bgcolor('black')
tr.pensize(1)
tr.pencolor('white')

""" rysowanie ramki """

tr.penup()
tr.goto(255, 255)
tr.left(180)

for k in range(0,4):
    for i in range(1, 7):
        tr.pendown()
        tr.forward(30)
        tr.penup()
        tr.forward(30)
        tr.pendown()
    tr.forward(30)
    tr.left(90)

tr.pensize(1)
tr.pencolor('red')

tr.penup()
for i in range(1, 7):
    tr.forward(30)
    tr.pendown()
    tr.left(90)
    tr.forward(390)
    tr.right(90)
    tr.forward(30)
    tr.right(90)
    tr.forward(390)
    tr.left(90)

tr.penup()
tr.forward(30)
tr.left(90)
tr.forward(30)

tr.pencolor('blue')
tr.pendown()
for k in range(1, 7):
    tr.left(90)
    tr.forward(390)
    tr.right(90)
    tr.forward(30)
    tr.right(90)
    tr.forward(390)
    tr.left(90)
    tr.forward(30)

tr.bgcolor('white')
for w in range(1, 5):
    tr.left(90)
    tr.forward(390)

tr.pencolor('yellow')
tr.pensize(2)
tr.penup()
tr.goto(-135, 255)
tr.pendown()

x = -135
y = 255
krok = 30
for krok in range(30, 390, 60):
    tr.goto(x, y - krok)
    tr.goto(x + krok, y)
    krok += 30
    tr.goto(x + krok, y)
    tr.goto(x, y - krok)

tr.penup()

tr.pencolor('green')
x = 255
y = 255
krok = 30
tr.goto(-135 + 30, -135)
tr.pendown()

for krok in range(30, 390, 60):
    tr.goto(-135 + krok, -135)
    tr.goto(x, y - krok)
    krok += 30
    tr.goto(x, y - krok)
    tr.goto(-135 + krok, -135)

tr.goto(x, -135)




def main():
    tr.setup()
    tr.done()
main()
