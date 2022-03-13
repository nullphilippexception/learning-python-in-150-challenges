import turtle
import random

scr = turtle.Screen()
turtle.pensize(5)

noOfLines = random.randint(1, 100)

for i in range(0, noOfLines):
    turtle.forward(random.randint(1, 50))
    turtle.right(random.randint(0, 360))

turtle.exitonclick()