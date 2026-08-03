import turtle

turtle.bgcolor("black")
turtle.speed(0.5)
turtle.penup()
turtle.goto(-210,50)
turtle.pendown()
for i in range(3) :
    for colour in ["red","orange","yellow","green","blue","violet","purple"] :
        turtle.color(colour)
        turtle.pensize(2)
        turtle.circle(100)
        turtle.forward(20)
