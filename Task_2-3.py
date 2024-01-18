# Посчитайте факториал введенного числа N

n = int(input('Введите число N: '))
fakt = 1
for i in range(1, n+1):
    fakt *= i
    print(fakt)