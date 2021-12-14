costs = [20, 22.5, 75, 1.49, 0.7, 43, 2435, 390, 180.9, 28]

for cost in costs:
    rub = int(cost // 1)
    kop = int((cost % 1) * 100)
    print(f'{rub:02} руб {kop:02} коп', end=', ')

print(f'\nпо возрастанию: {sorted(costs)}')
print(f'оригинал: {costs}')

costs_down = sorted(costs)
costs_down.reverse()
print(f'по убыванию: {costs_down}', end=', ')
print(f'\nсамые дорогие: {costs_down[:-5]}')
