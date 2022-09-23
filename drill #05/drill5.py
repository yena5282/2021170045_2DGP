import turtle

def left_move():
    turtle.setheading(180)
    turtle.forward(50)

def right_move():
    turtle.setheading(0)
    turtle.forward(50)

def up_move():
    turtle.setheading(90)
    turtle.forward(50)

def down_move():
    turtle.setheading(270)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(left_move, 'a')
turtle.onkey(right_move, 'd')
turtle.onkey(up_move, 'w')
turtle.onkey(down_move, 's')
turtle.onkey(restart, 'Escape')
turtle.listen()
