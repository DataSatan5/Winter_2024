# Ввести число N и напечатать для него таблицу умножения на числа от 1 до 9

n = int(input('Введите число N: '))
for i in range(1, 10):
    print(f'{i} x {n} = {i*n}')