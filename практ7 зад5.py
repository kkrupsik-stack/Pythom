matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print("Матрица 3x3:")
for row in matrix:
    print(row)

diagonal_sum = matrix[0][2] + matrix[1][1] + matrix[2][0]


print(f"\nСумма чисел по диагонали справа налево: {diagonal_sum}")
print(f"Расчёт: {matrix[0][2]} + {matrix[1][1]} + {matrix[2][0]} = {diagonal_sum}")
