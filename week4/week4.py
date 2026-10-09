#for i in(range(0, 100)):
#    print("We like Python's turtles!")
#for i in ["January", "February", "March"]:
#   print("One of the months of the year is", i)

#for i in [12,10,32,3,66,17,42,99,20]:
#    print(i)
#    print(i*i)
import turtle
# screen = turtle.Screen()
# ahmet = turtle.Turtle()
# for i in range(0, 3):
#     ahmet.forward(100)
#     ahmet.left(120)
# screen.exitonclick()
# screen = turtle.Screen()
# ahmet = turtle.Turtle()
# for i in range(0, 4):
#     ahmet.forward(100)
#     ahmet.left(90)
# screen.exitonclick()
# screen = turtle.Screen()
# ahmet = turtle.Turtle()
# for i in range(0, 6):
#     ahmet.forward(100)
#     ahmet.left(60)
# screen.exitonclick()
# screen = turtle.Screen()
# ahmet = turtle.Turtle()
# for i in range(0, 8):
#     ahmet.forward(100)
#     ahmet.left(45)
# screen.exitonclick()
# side = int(input("please select polygon side"))
# length = int(input("please select polygon length of side"))
# color = input("please select polygon color")
# screen = turtle.Screen()
# ahmet = turtle.Turtle()
# for i in range(0, side):
#     ahmet.begin_fill()
#     ahmet.fillcolor(color)
#     ahmet.forward(length)
#     ahmet.left(360/side)
# ahmet.end_fill()
# screen.exitonclick()

screen = turtle.Screen()

screen.bgcolor("lightgreen")

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(3)
t.stamp()
for i in range(12):
    t.penup()
    t.forward(100)
    t.pendown()
    t.forward(25)
    t.penup()
    t.forward(50)
    t.stamp()
    t.backward(175)
    t.left(30)




screen.exitonclick()