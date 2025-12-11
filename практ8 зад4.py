#1 вариант
all_d = {1: 15, 4: 80, 44: 0, 256: 15, 100: 70, 101: 70, 20: 44, 3: 9}

del all_d[1]
del all_d[101]
del all_d[3]

print(all_d)
#вариант 2
all_d = {1: 15, 4: 80, 44: 0, 256: 15, 100: 70, 101: 70, 20: 44, 3: 9}

all_d.pop(1)
all_d.pop(101)
all_d.pop(3)

print(all_d)
