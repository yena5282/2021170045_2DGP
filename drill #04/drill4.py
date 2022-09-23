Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle

turtle.penup()
turtle.goto(300, 300)
turtle.pendown()

a = 1
while(a <= 4):
    turtle.right(90)
    turtle.forward(500)
    a = a + 1

    
b = 1
while(b <= 2):
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    b = b+1

    
turtle.right(90)
turtle.forward(100)


c = 1
while(c <= 2):
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    c = c+1

    
