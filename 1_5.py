numA = ord(input("Введите первую букву:").lower())
numB = ord(input("Введите вторую букву:").lower())
if numA == numB:
    print("Введена одна буква")
else:
    if numB < numA:
        numA_old = numA
        numA = numB
        numB = numA_old
    pos_a = numA - ord("a") + 1
    pos_b = numB - ord("a") + 1
    dist = pos_b - pos_a - 1
    print(f"Буква {chr(numA)} на {pos_a} месте, буква {chr(numB)} на {pos_b} месте")
    if dist == 0:
        answer = "нет букв"
    elif dist == 1:
        answer = str(dist) + " буква"
    elif dist >= 2 and dist <=4:
        answer = str(dist) + " буквы"
    print(f"между ними {answer}")