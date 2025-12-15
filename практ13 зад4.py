def begin(field, row, col):
    field[row][col] = '*'
    return field  
field = [['[ ]', '[ ]', '[ ]'],
         ['[ ]', '[ ]', '[ ]'],
         ['[ ]', '[ ]', '[ ]']]


result = begin(field, 1, 2)

for row in result:
    print(row)
