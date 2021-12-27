def odd_nums(max_val):
    gen_nums = (num for num in range(1, max_num + 1, 2))
    return gen_nums


max_num = int(input("Максимальное число:"))
generated_nums = odd_nums(max_num)
print(type(generated_nums))
for g_num in generated_nums:
    print(g_num)
