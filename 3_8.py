table = [[],[],[],[]]
for row in range(4):
    for column in range(5):
        if column < 4:
            table[row].append(int(input(f'Строка {row+1} столбец {column+1}:')))
        else:
            table[row].append(sum(table[row]))
for row in table:
    print(row)