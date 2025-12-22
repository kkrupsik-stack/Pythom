
numbers = []

while len(numbers) < 5:
    user_input = input(">>> ")

    if user_input.lstrip('-').replace('.', '').isdigit():
     
        if '.' in user_input:
            numbers.append(float(user_input))
        else:
            numbers.append(int(user_input))
    else:
    
        print(f"Не число, пропускаем: {user_input}")
        continue
print(">>> Числа в списке: ", numbers)
