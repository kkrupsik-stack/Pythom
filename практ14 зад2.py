numbers = [4, 3.2, 16, 9, 13.5, 67]

for index, value in enumerate(numbers):
    try:
     
        if index == 0:
            raise ZeroDivisionError 
        result = value / index
        print(f"{value} / {index} = {result}")
    except ZeroDivisionError:
        print(f!Деление на 0! Элемент: {value}")
