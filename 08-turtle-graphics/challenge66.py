import turtle
import random

scr = turtle.Screen()
turtle.pensize(5)
colors = ["yellow", "blue", "red", "green", "orange", "pink"]

for i in range(0, 8):
    turtle.color(colors[random.randint(0, 5)])
    turtle.forward(100)
    turtle.right(45)

turtle.exitonclick()