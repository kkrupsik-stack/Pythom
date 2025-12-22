import random

# Определяем элементы для двух типов фигур
figure_elements_1 = ['Г', '7', '3', 'Л']  # Фигура 1 (как в задании)
figure_elements_2 = ['(', ')', '{', '}']  # Фигура 2 (альтернативная)

# Правильные конфигурации (целевые фигуры)
target_figure_1 = ['Г', '7', '3', 'Л']
target_figure_2 = ['(', ')', '{', '}']

# Функция для генерации случайной фигуры
def generate_random_figure():
    return random.choice([figure_elements_1, figure_elements_2])

# Функция для вывода текущей фигуры
def print_figure(figure):
    print(f"Текущая фигура: {figure[0]} {figure[1](https://PythonRu.com/biblioteki/pyplot-uroki)}")
    print(f"                {figure[2](https://github.com/vabobkov1999/Generation-and-recognition-of-shapes)} {figure[3](https://reshak.ru/otvet/reshebniki.php?otvet=4-4/8&predmet=bosova_new8)}")

# Функция для проверки, собрана ли правильная фигура
def is_correct(figure, target):
    return figure == target

# Основная логика игры
def main():
    print("Цель: собрать правильную фигуру!")
    print("Используйте цифры 1-4 для замены элементов фигуры.")
    print("Фигура будет генерироваться заново при каждом запуске.\n")

    # Генерируем случайную фигуру
    current_figure = generate_random_figure()
    target_figure = target_figure_1 if current_figure == figure_elements_1 else target_figure_2

    # Выводим подсказку (правильную фигуру)
    print("Подсказка (правильная фигура):")
    print_figure(target_figure)

    # Игровой цикл
    while True:
        print("\n" + "-" * 30)
        print_figure(current_figure)

        # Получаем ввод от пользователя
        choice = input("\nВведите номер элемента для изменения (1-4) или 'q' для выхода: ")

        if choice.lower() == 'q':
            print("Игра окончена.")
            break

        if choice.isdigit() and 1 <= int(choice) <= 4:
            element_index = int(choice) - 1
            # Генерируем новый случайный элемент для выбранного места
            new_elements = figure_elements_1 if current_figure == figure_elements_1 else figure_elements_2
            current_figure[element_index] = random.choice(new_elements)

            # Проверяем, собрана ли правильная фигура
            if is_correct(current_figure, target_figure):
                print("\n🎉 Поздравляем! Вы собрали правильную фигуру!")
                print_figure(current_figure)
                break
        else:
            print("Ошибка: введите число от 1 до 4 или 'q' для выхода.")

if __name__ == "__main__":
    main()
