lenght1 = int(input("Введите длину 1 отрезка:"))
lenght2 = int(input("Введите длину 2 отрезка:"))
lenght3 = int(input("Введите длину 3 отрезка:"))

if (lenght1 >= lenght2 + lenght3) or (lenght2 >= lenght1 + lenght3) or (lenght3 >= lenght1 + lenght2):
    print("Такой треугольник невозможен")
else:
    if lenght1 == lenght2:
        if lenght1 == lenght3:
            print("треугольник равносторонний")
        else:
            print("треугольник равнобедренный")
    elif lenght2 == lenght3 and lenght2 !=lenght1:
        print("треугольник равнобедренный")
    elif lenght1 == lenght3 and lenght1 != lenght2:
        print("треугольник равнобедренный")
    else:
        print("треугольник разносторонний")
