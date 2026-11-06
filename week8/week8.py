# def findHypot(side1, side2):
#     print ((side1 ** 2 + side2 ** 2) ** 0.5)
#
# kenar1 = int(input("1. kenari giriniz "))
# kenar2 = int(input("2. kenari giriniz "))
# findHypot(kenar1, kenar2)
#
# mark = int(input("please enter your mark: "))
# if mark >= 90:
#     print("A")
# elif 90 > mark >= 80:
#     print("B")
# elif 80 > mark >= 70:
#     print("C")
# elif 70 > mark >= 60:
#     print("D")
# elif 60 > mark:
#     print("D")
import turtle

def chooseColor(t, height1):
    if height1 >= 200:
         t.color("red")
    elif 200 > height1 >= 100:
        t.color("yellow")
    else:
        t.color("green")

def drawBarChart(t, height1):
    chooseColor(t, height1)
    t.begin_fill()
    t.left(90)
    t.forward(height1)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(height1)
    t.left(90)
    t.end_fill()
def BarChart(t, list1):
    for i in list1:
        drawBarChart(t, i)

wn = turtle.Screen()
list = [50, 70, 150, 20, 200]
BarChart(turtle, list)
wn.exitonclick()