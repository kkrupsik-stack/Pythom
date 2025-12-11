
my_dict = {}

while len(my_dict) < 3:

    key = input("Введите ключ (число): ")
    
    if not key.isdigit():
        print("Ошибка! Ключ должен быть числом. Попробуйте ещё раз.")
        continue 
    
    key = int(key)  

    value = input("Введите значение: ")

    my_dict[key] = value
    
    print(f"Текущий словарь: {my_dict}")


print("Финальный словарь:", my_dict)
