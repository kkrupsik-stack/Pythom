m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']
figures = m.copy()
for item in m:

    if not isinstance(item, str):
    
        while item in figures:
            figures.remove(item)

    elif item == '10':
        while item in figures:
            figures.remove(item)

print("Исходный массив:")
print(m)

print("\nМассив только с названиями фигур:")
print(figures)

print("\n--- Альтернативное решение ---")

figures_list = ['круг', 'квадрат', 'треугольник', 'овал']
result = []

for item in m:
    if isinstance(item, str) and item in figures_list:
        result.append(item)
print("Результат (альтернативный способ):")
print(result)
