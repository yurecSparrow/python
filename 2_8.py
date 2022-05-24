def count_digit_in(digit, value):
    if value > 0:
       if value % 10 == digit:
           return count_digit_in(digit,(value//10))+1
       else:
           return count_digit_in(digit,(value//10))
    else:
        return 0

digit_to_count = int(input("Какую цифру будем считать?:"))
numbers_count = int(input("Сколько чисел будем вводить?:"))
sum_of_digits = 0
for i in range(numbers_count):
    number = int(input(f"Число {i+1} из {numbers_count}:"))
    sum_of_digits += count_digit_in(digit_to_count,number)
print(f"Цифра {digit_to_count} встречалась {sum_of_digits} раз")
