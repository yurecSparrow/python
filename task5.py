src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_nums = set()
tmp = set()
for num in src:
    if num not in tmp:
        unique_nums.add(num)
    else:
        unique_nums.discard(num)
    tmp.add(num)
unique_nums_ord = [ord_num for ord_num in src if ord_num in unique_nums]
print(unique_nums_ord)
