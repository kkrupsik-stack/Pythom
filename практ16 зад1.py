import random

left_turns = 0  
straight_moves = 0  
right_turns = 0  
print("Начинаем игру. Повороты: [a] — Налево, [w] — Прямо, [d] — Направо. Куда идти?")

while True:
    user_input = input().lower()
а
    if user_input not in ['a', 'w', 'd']:
        print(f"Некорректный ввод: '{user_input}'. Используйте [a], [w] или [d].")
        continue

    if user_input == 'a':
        left_turns += 1
        print("Повернул налево. Выхода пока нет… Куда идти?")
    elif user_input == 'w':
        straight_moves += 1
        print("Пошёл прямо. Выхода пока нет… Куда идти?")
    elif user_input == 'd':
        right_turns += 1
        print("Повернул направо. Выхода пока нет… Куда идти?")

    if random.randint(1, 10) == 1:
        print(f"Выход найден. Ты выиграл!\n"
              f"Для того, чтобы найти выход, ты:\n"
              f"- {left_turns} раз повернул налево,\n"
              f"- {straight_moves} раз пошёл прямо,\n"
              f"- {right_turns} раз повернул направо.")
        break
