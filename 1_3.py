dotA_x = int(input("Введите Ax:"))
dotA_y = int(input("Введите Ay:"))
dotB_x = int(input("Введите Bx:"))
dotB_y = int(input("Введите By:"))
if dotA_x == dotB_x and dotA_y != dotB_y:
    print("Прямая не являеться функцией")
elif dotA_x == dotB_x and dotA_y == dotB_y:
    print("Введены координаты одной точки")
else:
    coef_k = (dotA_y - dotB_y) / (dotA_x - dotB_x)
    coef_b = dotA_y - coef_k * dotA_x
    if coef_k % 1 == 0 :                    #Убираем 0 после запятой, если k целое число
        coef_k = int(coef_k)
    if coef_b % 1 == 0 :                    #Убираем 0 после запятой, если b целое число
        coef_b = int(coef_b)
    if coef_k != 0:                         #Если k не равен нулю, то выводим kx
        func_answer = str(coef_k)+"x"
    else:func_answer = ""                   #Если k равен нулю, то ничего не выводим (избавляемся от 0x в ответе)
    if coef_b > 0:
        if coef_k != 0:                     #Если выводим kx, то дописываем к b знак +
            func_answer2 = "+"+(str(coef_b))
        else:                               #Если не выводим kx (0x), то выводим b как есть
            func_answer2 =str(coef_b)
    elif coef_b < 0:                        #Если b меньше нуля выводим как есть
        func_answer2 = str(coef_b)
    else:                                   #Если b равен нулю, то ничего не выводим (избавляемся от +0 в ответе)
        func_answer2 = ""
    print(f"y={func_answer}{func_answer2}")
