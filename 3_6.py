from random import randint

arr_random = [randint(0, 100) for i in range(10)]
value_min = min(arr_random)
value_max = max(arr_random)
index_min = -1
index_max = -1
for i in range(len(arr_random)):
    if arr_random[i] == value_max:
        index_max = i
    if arr_random[i] == value_min:
        index_min = i
    if index_max !=-1 and index_min !=-1:
        break
index_begin = min(index_min, index_max) + 1
index_end = max(index_min, index_max)
sum_between = sum(arr_random[index_begin:index_end])
print(f'Массив:{arr_random}')
print(f'Сумма элементов между минимальным ({value_min}) и максимальным ({value_max}):{sum_between}')
