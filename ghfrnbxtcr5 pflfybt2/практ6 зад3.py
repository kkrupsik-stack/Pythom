fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], ['lime', 'lemon'], ['Mango', 'grapes']]

capitalized_fruits = []

for row in fruits:
    for fruit in row:
квы
        if fruit and fruit[0].isupper():
            capitalized_fruits.append(fruit)


print("Элементы с заглавной буквы:", capitalized_fruits)
