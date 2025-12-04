number = int(input("введите целое число:")) 
if number < 0:
    number = abs(number)
elif number == 0:
    number = 1 

print("Результат:", number)
