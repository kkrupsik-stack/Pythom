matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]

answer_matrix = []
for i in range(len(matrix_1)):
    row = []
    for j in range(len(matrix_1[i])):
        row.append(0)
    answer_matrix.append(row)

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[i])):
        answer_matrix[i][j] = matrix_1[i][j] * matrix_2[i][j]

print(answer_matrix)


for row in answer_matrix:
    row_sum = sum(row)
    print(f"{row} сумма строки: {row_sum}")
