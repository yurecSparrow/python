from random import randint

arr_input = [randint(1,100) for i in range(10)]
arr_even = []
print(f'Массив:{arr_input}')
for i in range(10):
    if arr_input[i] % 2 == 0:
        arr_even.append(i)
print(f'Индексы четных элементов:{arr_even}')