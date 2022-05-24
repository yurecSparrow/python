from random import randint

random_number = randint(0, 100)
for i in range(10):
    user_number = int(input(f"Попытка {i+1}, введите число:"))
    if user_number == random_number:
        print(f"Поздравляю, вы угадали загаданное число за {i+1} попыток")
        break
    if user_number > random_number:
        print(f"Нет, число {user_number} больше загаданного")
    if user_number < random_number:
        print(f"Нет, число {user_number} меньше загаданного")
if user_number != random_number:
    print(f"К сожалению попытки закончились, было загадано число {random_number}")