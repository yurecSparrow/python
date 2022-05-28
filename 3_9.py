from random import randint

table = []
rows = randint(2,10)
columns = randint(2,10)
for row in range(rows):
    table.append([randint(0,100) for column in range(columns)])
for row in table:
    print(row)
min_values = []
for column in range(columns):
    min_values.append(min(table[row][column] for row in range(rows)))
print('Минимальные значения в столбцах:')
print(min_values)
max_from_min = max(min_values)
print(f'Из них максимальное:{max_from_min}')
