import turtle

scr = turtle.Screen()
turtle.pensize(2)

for i in range(0, 10):
    for j in range(0, 8):
        turtle.forward(100)
        turtle.right(45)
    turtle.right(36)

turtle.exitonclick()
