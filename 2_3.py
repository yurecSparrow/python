def mirror_num(num):
    if num > 0:
        return ((num%10)+mirror_num(num//10))/10
    else:
        return 0

user_number = int(input("Введите число:"))
reversed_number = mirror_num(user_number)
while (reversed_number%1)>0:
    reversed_number *= 10
reversed_number = int(reversed_number)
print(reversed_number)
