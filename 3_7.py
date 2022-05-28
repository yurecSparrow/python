from random import randint

arr_random = [randint(0, 10) for i in range(10)]
first_min_index = arr_random.index(min(arr_random))
first_min_value = arr_random[first_min_index]
arr_random[first_min_index] = max(arr_random)
second_min_index = arr_random.index(min(arr_random))
second_min_value = arr_random[second_min_index]
arr_random[first_min_index] = first_min_value
print(f'массив:{arr_random}')
print('Наименьшие элементы массива:')
print(f'{first_min_value} позиция {first_min_index+1}')
print(f'{second_min_value} позиция {second_min_index+1}')
