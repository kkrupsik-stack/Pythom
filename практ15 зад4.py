def ellipse(a, b, tilt=0, color='black', fill=''):
    turtle.color(color)
    turtle.fillcolor(fill)
    turtle.left(tilt)  # Наклон эллипса (по умолчанию 0°)
    turtle.begin_fill()
    turtle.circle(a, 45)
    turtle.circle(b, 90)
    turtle.circle(a, 90)
    turtle.circle(b, 90)
    turtle.circle(a, 45)
    turtle.end_fill()
    turtle.right(tilt)  # Возвращаем черепашку в исходное положение

# Примеры вызова функции:
ellipse(150, 60)           # Эллипс без наклона, чёрный контур
ellipse(120, 50, tilt=25)  # Эллипс с наклоном 25°
ellipse(100, 35, color='blue', fill='orange')  # Синий контур, оранжевая заливка
