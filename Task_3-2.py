y = input('Введите число и нажмите Enter: ')
digits = '0123456789'
for num in range(0, 10):
    cifr = digits[num]
    print(cifr, '-', y.count(cifr))