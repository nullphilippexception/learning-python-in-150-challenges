import turtle

scr = turtle.Screen()
turtle.pensize(5)

# draw 1
turtle.left(90)
turtle.forward(100)

# go to and draw 2
turtle.penup()
turtle.right(90)
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

# go to and draw 3
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(35)
turtle.penup()
turtle.forward(15)
turtle.right(90)
turtle.forward(50)
turtle.pendown()
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

turtle.exitonclick()