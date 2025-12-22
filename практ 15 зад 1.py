import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.speed(1)

for i in range(4):
    t.forward(150) 
    t.left(90)    

turtle.exitonclick()
