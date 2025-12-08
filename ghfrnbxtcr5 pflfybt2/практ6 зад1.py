matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("matrix:")
for row in matrix:
    print(row)

odd_numbers = []
for row in matrix:
    for num in row:
        if num % 2 != 0:
            odd_numbers.append(num)

print("\nнечётные числа matrix")
print(*odd_numbers)

even_count = 0
for row in matrix:
    for num in row:
        if num % 2 == 0:
            even_count += 1

print(f"\nкол-во чётных: {even_count}")
