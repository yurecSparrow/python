digit = 0
while digit < 100 or digit > 999:
    digit = int(input("Введите трехнзначное число:"))
summ_of_digits = digit % 10 + digit % 100 // 10 + digit //100
multip_of_digits = (digit % 10) * (digit % 100 // 10) * (digit //100)
print(f"Сумма цифр числа {digit} равна {summ_of_digits}, прозведение равно {multip_of_digits}")