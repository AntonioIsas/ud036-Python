import turtle
def draw_square(someTurtle):
    for i in range(1,5):
        someTurtle.forward(100)
        someTurtle.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()

    for i in range(1, 37):
        draw_square(brad)
        brad.right(10)

    angie = turtle.Turtle()
    angie.circle(100)
    
    window.exitonclick()

draw_art()
