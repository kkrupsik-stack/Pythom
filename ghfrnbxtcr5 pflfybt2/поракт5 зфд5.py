# Инициализируем списки
negatives = []
positives = []
zeros = []

# Ввод количества чисел
n = int(input("Введите количество чисел: "))

# Ввод чисел и распределение
for i in range(n):
    num = float(input("Введите числа: "))
    if num < 0:
        negatives.append(num)
    elif num > 0:
        positives.append(num)
    else:
        zeros.append(num)

print("Отрицательные:", negatives)
print("Положительные:", positives)
print("Нули:", zeros)
