from random import randint

arr_random = [randint(1,100) for i in range(10)]
print(f'Исходный массив:{arr_random}')
element_max = 0
element_min = arr_random[0]
index_min = 0
index_max = 0
for i in range(10):
    if arr_random[i] < element_min:
        index_min = i
        element_min = arr_random[i]
    if arr_random[i] > element_max:
        index_max = i
        element_max = arr_random[i]
arr_random[index_max] = element_min
arr_random[index_min] = element_max
print(f'Результат:{arr_random}')
