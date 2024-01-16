# Задание 1-2
# Вводится два числа x и y. Вывести наибольшее из чисел: x+y, x-y, x*y, x/y, x//y

x = float(input('Введите число x: '))
y = float(input('Введите число y: '))

print('************************************************')
print('Наибольшее число среди x+y, x-y, x*y, x/y, x//y это: ', end='')

if  (x + y) > (x - y): # Сравнение первый пары чисел
    max1 = x + y
else:
    max1 = x - y
if (x / y) > (x // y): # Сравнение второй пары чисел
    max2 = x / y
else:
    max2 = x // y
if max1 > max2: # Сравнение "победителей" предыдущих сравнений между собой и с перемножением
    if max1 > x * y:
        print(max1)
    else:
        print(x * y)
else:
    if max2 > x * y:
        print(max2)
    else:
        print(x * y)