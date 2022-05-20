numA = int(input("Введите число a:"))
numB = int(input("Введите число b:"))
numC = int(input("Введите число c:"))

num_max = max(numA, numB, numC)
num_min = min(numA, numB, numC)

if numA < num_max and numA > num_min:
    print(f"Среднее число:{numA}")
elif numB < num_max and numB > num_min:
    print(f"Среднее число:{numB}")
elif numC < num_max and numC > num_min:
    print(f"Среднее число:{numC}")
else:
    print("Нельзя найти среднее число")