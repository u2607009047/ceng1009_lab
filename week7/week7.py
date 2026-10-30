# def sumTo(n):
#     total = n * (n + 1) / 2
# #     return total
# # print(sumTo(10))
# import turtle
#
#
# def drawStar(t, n, size):
#     angle = 180 - 180 / n
#     for i in range(n):
#         t.forward(size)
#         t.right(angle)
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
# drawStar(t, 11, 100)
# wn.exitonclick()
#
# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
# print(sumTo(100))
import turtle


# def approx(x):
#     guess = x / 2
#     for i in range(20):
#         guess = (1/2) * (guess + x / guess)
#         print(guess)
#     return guess
#
# n = int(input("Enter a positive integer: "))
# print(approx(n))
# def drawSprite(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
#
# def fancySquare(t, size):
#     for corner in range(4):
#         drawSprite(t, 8, 28)
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.color("hotpink")
# fancySquare(t, 100)

# def drawTip(t, size):
#     t.begin_fill()
#     t.left(90)
#     t.forward(size / 2)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size / 2)
#     t.right(90)
#     t.end_fill()
#
# def drawSpriteWithTips(someturtle , legs , length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(length)
#         drawTip(someturtle, 10)
#         someturtle.backward(length)
#         someturtle.left(angle)
# def fancySquare(t, size):
#     for corner in range(4):
#         drawSpriteWithTips(t, 8, 20)
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("black")
# t = turtle.Turtle()
# t.color("white")
#
# fancySquare(t, 100  )
#
# wn.exitonclick()
# import math
# number = input("Enter a number: ")
# if int(number) < 0:
#     print("negative number")
# if int(number) > 0:
#     print("positive number")
# if int(number) == 0:
#     print("zero")
data = [48, 117, 200, 240, 160]
def drawbar(t1, length, width):
    for i in length:
        t1.begin_fill()
        t1.left(90)
        t1.forward(i)
        t1.right(90)
        t1.forward(width)
        t1.right(90)
        t1.forward(i)
        t1.left(90)
        t1.end_fill()
wn = turtle.Screen()
t = turtle.Turtle()
drawbar(t, data, 10)


wn.exitonclick()