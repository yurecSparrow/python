from random import randint

arr_random = [randint(-100, 100) for i in range(20)]
print(f'Массив:{arr_random}')
max_val = min(arr_random)
index_max = -1
for i in range(len(arr_random)):
    if max_val<arr_random[i]<0:
        max_val = arr_random[i]
        index_max = i
if index_max != -1:
    print(f'Максимальное отрицательное число:{max_val}, его позиция:{index_max+1}')
else:
    print('Отрицательные числа отсутствуют')
