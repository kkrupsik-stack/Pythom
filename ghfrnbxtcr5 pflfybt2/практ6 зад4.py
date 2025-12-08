random_elements = [
    ['toy', 'bee', 'cheese', 'ear'],
    [False, 'word', '0110110', 10],
    ['happiness', '(J ^口^)J ', 'luck', None],
    ['car', '<- code ->', 4.7, True]
]

for row_index, row in enumerate(random_elements):
  
    for col_index, element in enumerate(row):

        if col_index % 2 == 0:
            print(f"Элемент с индексом {col_index} в строке {row_index}: {element}")
