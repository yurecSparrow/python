n=int(input("Введите натуральное число:"))
summ = 0
for i in range(n):
    summ+=(i+1)
fast = n *(n+1)/2
print(f"Сумма равна {summ}, n*(n+1)/2={fast}")