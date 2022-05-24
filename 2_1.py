while True:
    operation_sign = input("Введите знак операции (+, -, *, /, 0 - выход):")
    if operation_sign == "0":
        break
    if operation_sign in "+-*/":
        first_num = float(input("Введите первое число:"))
        second_num =float(input("Введите второе число:"))
        if second_num == 0:
            print(f"Деление на ноль невозможно")
        else:
            result = 0;
            if operation_sign == "+":
                result = first_num + second_num
            elif operation_sign == "-":
                result = first_num - second_num
            elif operation_sign == "*":
                result = first_num * second_num
            else:
                result = first_num / second_num
            print(result)
    else:
        print("Неверный знак операции")
