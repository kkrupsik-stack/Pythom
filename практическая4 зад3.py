num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число"))
if num1 % 3 == 0 and num2 % 3 == 0:
    result = True
elif num1 % 3 == 0 or num2 % 3 == 0:
    result = "одно число делится на 3"
else:
    result = False
    print(result)
