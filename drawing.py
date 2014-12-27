import turtle

def draw():
    window = turtle.Screen()

    shape = turtle.Turtle()
    shape.speed(50)
    shape.home()
    for i in range(1,37):
        shape.circle(50)
        shape.rt(10)

    shape.rt(90)
    shape.fd(200)
    window.exitonclick()

draw()
