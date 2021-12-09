idx = 1
while idx <= 1000:
    if idx % 10 == 1 and idx != 11:
        print(idx, 'процент')
    elif (idx % 10 == 2 or idx % 10 == 3 or idx % 10 == 4) and (idx != 12 and idx != 13 and idx != 14):
        print(idx, 'процента')
    else:
        print(idx, 'процентов')
    idx += 1
    