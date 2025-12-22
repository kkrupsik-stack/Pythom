import turtle

t = turtle.Turtle()

# Перемещение в первую вершину без рисования
t.penup()
t.goto(0, 0)
t.pendown()

# Рисование треугольника
t.goto(100, 0)
t.goto(50, 100)
t.goto(0, 0)

turtle.done()
