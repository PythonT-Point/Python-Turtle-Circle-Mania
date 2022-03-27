from turtle import *
import turtle
ptp = turtle.Screen()
ptp.bgcolor('black')
ptp.title("Pythontpoint")
ws = turtle.Turtle()
ws.speed('fastest')
ws.color('light blue')
rotate=int(180)
def circlemania(tur,siz):
    for i in range(12):
        tur.circle(siz)
        siz=siz-6
def ptp1(tur,siz,repet):
  for x in range (repet):
    circlemania(tur,siz)
    tur.right(360/repet)
ptp1(ws,202,12)
tur1 = turtle.Turtle()
tur1.speed(0)
tur1.color('pink')
rotate=int(90)
def circlemania(tur,siz):
    for x in range(6):
        tur.circle(siz)
        siz=siz-12
def ptp1(tur,siz,repet):
    for x in range (repet):
        circlemania(tur,siz)
        tur.right(360/repet)
ptp1(tur1,162,12)
tur2= turtle.Turtle()
tur2.speed(0)
tur2.color('green')
rotate=int(80)
def circlemania(tur,siz):
    for x in range(6):
        tur.circle(siz)
        siz=siz-7
def ptp1(tur,siz,repet):
    for x in range (repet):
        circlemania(tur,siz)
        tur.right(360/repet)
ptp1(tur2,122,12)
tur3 = turtle.Turtle()
tur3.speed(0)
tur3.color('yellow')
rotate=int(90)
def circlemania(tur,siz):
    for x in range(6):
        tur.circle(siz)
        siz=siz-21
def ptp1(tur,siz,repet):
    for x in range (repet):
        circlemania(tur,siz)
        tur.right(360/repet)
ptp1(tur3,82,12)
tur4= turtle.Turtle()
tur4.speed(0)
tur4.color('orange')

rotate=int(90)
def circlemania(tur,siz):
    for x in range(6):
        tur.circle(siz)
        siz=siz-22
def ptp1(tur,siz,repet):
    for x in range (repet):
        circlemania(tur,siz)
        tur.right(360/repet)
ptp1(tur4,42,12)
ptp.exitonclick()