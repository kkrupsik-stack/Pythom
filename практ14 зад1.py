while True:
    user_input = input("число: ")
    
    if user_input.isdigit() and int(user_input) > 0:
        x = int(user_input)
        print(" ".join(map(str, range(x + 1))))
        break  
    else:
        print(f"{user_input} - не число. Повторите ввод.")
