import turtle
import time

# outside line
turtle.pensize(5)
turtle.goto(0, 0)
turtle.pendown()
for _ in range(4):
    turtle.forward(270)
    turtle.right(90)
print(turtle.pos())


# 3*3 line
turtle.speed(0)
turtle.pensize(3)
for y in range(0,-270,-90):
    turtle.home()
    for x in range(0,270,90):
        turtle.goto(x , y)
        print(turtle.pos())
        turtle.pendown()
        for _ in range(4):
            turtle.forward(90)
            turtle.right(90)
        turtle.penup()


# inside line
turtle.pensize(1)
for y in range(0,-270,-30):
    turtle.home()
    for x in range(0,270,30):
        turtle.goto(x , y)
        print(turtle.pos())
        turtle.pendown()
        for _ in range(4):
            turtle.forward(30)
            turtle.right(90)
        turtle.penup()




turtle.done()