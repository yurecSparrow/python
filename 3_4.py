from random import randint

arr_random = [randint(1,10) for i in range(20)]
repeats = {}
for i in range(len(arr_random)):
    if arr_random[i] not in repeats.keys():
        repeats[arr_random[i]] = 1
    else:
        repeats[arr_random[i]] += 1
print(f'Массив:{arr_random}')
print(f'Повторения:{repeats}')
lst_max_repeats = []
max_repeats = max(repeats.values())
for i in repeats.keys():
    if repeats[i] == max_repeats:
        lst_max_repeats.append(i)
print(f'Больше повторов у следующих чисел: {lst_max_repeats}')
