
bin_sy = ['1101111', '11011101', '11000111', '11011100', '11011110']


decimal_numbers = []


for binary_num in bin_sy:

    decimal_num = int(binary_num, 2)
    decimal_numbers.append(decimal_num)

    print(f"Двоичное число {binary_num} в десятичной системе: {decimal_num}")

max_number = max(decimal_numbers)
min_number = min(decimal_numbers)

print(f"\nМаксимальное число: {max_number}")
print(f"Минимальное число: {min_number}")
