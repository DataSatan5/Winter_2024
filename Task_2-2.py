# Задать массив из чисел. Найти минимальный элемент без встроенных сортировок и поисков min/max

print('Введите через пробел элементы массива. \nПосле нажатия Enter ввод будет прекращен.\n')
lst = [int(x) for x in input().split()]

min = lst[0]
for num in lst:
    if num < min:
        min = num
print(min)