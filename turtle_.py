import random
import turtle
t = turtle.Turtle()
for i in range(10):
    t.color("black", "green")
    t.begin_fill()
    t.begin_poly()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
for i in range(10):
    #t.color("red", "green", "blue", "black", "cyan", "grey", "white")
    if i == 0:
        t.color("white", "grey")
    if i == 1:
        t.color("white", "red")
    if i == 2:
        t.color("white", "blue")
    if i == 3:
        t.color("white", "green")
    if i == 4:
        t.color("white", "cyan")
    if i == 5:
        t.color("white", "yellow")
    if i == 6:
        t.color("white", "purple")
    if i == 7:
        t.color("white", "brown")
    if i == 8:
        t.color("white", "orange")
    if i == 9:
        t.color("white", "black")
    t.begin_fill()
    t.forward(10)
    t.left(22)
    t.forward(10)
    t.right(22)
    t.circle(25)
    t.end_fill()