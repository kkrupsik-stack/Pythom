import turtle

# Создаём экран и черепашку
screen = turtle.Screen()
t = turtle.Turtle()

# Устанавливаем цвет заливки (например, красный)
t.fillcolor("red")

# Начинаем заливку фигуры
t.begin_fill()

# Рисуем звезду
for i in range(5):
    t.forward(100)  # Двигаемся вперёд на 100 пикселей
    t.right(144)    # Поворачиваем направо на 144 градуса (ключевой угол для звезды)

# Завершаем заливку
t.end_fill()

# Держим окно открытым до клика
turtle.exitonclick()
