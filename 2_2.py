number = int (input("Введите натуральное число:"))
even = 0
not_even = 0
while number != 0:
    if number % 2 == 0:
        even += 1
    else:
        not_even += 1
    number //= 10
print(f"{even} четных, {not_even} нечетных")
