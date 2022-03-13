import turtle

scr = turtle.Screen()
turtle.pensize(5)
colorlist = ["blue","red","yellow"]

for i in range(0, 3):
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black", colorlist[i])
    for j in range(0, 4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(200)
turtle.exitonclick()