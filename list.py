c_list = []
idx = 1
while idx <= 1000:
    if idx % 2 != 0:
        c_list.append(idx ** 3)
    idx += 1

total = 0
idx = 1
while idx <= 2:
    jdx = 0
    while jdx < len(c_list):
        if (c_list[jdx] // 1000 + c_list[jdx] % 1000 // 100 + c_list[jdx] % 100 // 10 + c_list[jdx] % 10) % 7 == 0:
            total += c_list[jdx]
        c_list[jdx] += 17
        jdx += 1
    print('сумма = ', total)
    total = 0
    idx += 1
