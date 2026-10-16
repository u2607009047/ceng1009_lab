 # import random
# #
# # for i in range(10):
# #     print(random.random())
# #
# # for i in range(10):
# #     print(random.randint(25,35))
import math
#
# a = int(input("enter a:"))
# b = int(input("enter b:"))
# c = math.sqrt(a**2 + b**2)
# # print(c)
# def areaofcircle(radius):
#     radius = float(input("Enter the radius of the circle: "))
#     return math.pi * radius * radius
#
# print(areaofcircle(0))
import turtle
#
# def drawstar(t, side):
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
# drawstar(tess, 100)
# screen.exitonclick()


def drawsquare(t, side):
    for i in range(4):
        t.forward(side)
        t.left(90)

# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.color("pink")
# tess.pensize(3)
#
# for i in range(5):
#     drawsquare(tess, 20)
#     tess.penup()
#     tess.forward(30)
#     tess.pendown()
# screen.exitonclick()
tess = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("lightgreen")
tess.color("blue")
tess.pensize(5)
for i in range(20, 120, 20):
    drawsquare(tess, i)
    tess.penup()
    tess.backward(10)
    tess.right(90)
    tess.forward(10)
    tess.left(90)
    tess.pendown()
screen.exitonclick()
