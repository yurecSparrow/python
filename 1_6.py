letter_num = 27
while letter_num > 26 or letter_num < 1:
    letter_num = int(input("Введите номер буквы (от 1 до 26):"))
print(f"Это буква {chr(ord('a') + letter_num - 1)}")
