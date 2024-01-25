ch = int(input('Введите число, делители которого необходимо найти:  '))
res = []
for i in range(1, round(ch/2) + 1):
    if ch % i == 0:
        res.append(i)
res.append(ch)
print(res)