import random

numA = int (input("Введите целое число A:"))
numB = int (input("Введите целое число B:"))
print(f"Случайное целое число:{random.randint(numA,numB)}")

numA = float(input("Введите вещественное число А:"))
numB = float(input("Введите вещественное число B:"))
print(f"Случайное вещественное число:{random.uniform(numA,numB)}")

numA = ord(input("Введите первую букву:"))
numB = ord(input("Введите вторую букву:"))
print(f"Случайная буква:{chr(random.randint(numA,numB))}")
