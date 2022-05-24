def get_dig_sum(number):
    if number > 0:
        return number % 10 + get_dig_sum(number // 10)
    else:
        return 0

max_sum = 0;
max_sum_number = 0;
while True:
    user_number = int(input("Введите натуральное число, для окончания ввода введите 0:"))
    if user_number == 0:
        break
    if get_dig_sum(user_number) > max_sum:
        max_sum_number = user_number
        max_sum = get_dig_sum(user_number)
print(f"У числа {max_sum_number} самая большая сумма ({max_sum}) цифр")
