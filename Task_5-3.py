n = int(input('введите число, до которого продолжается последовательность Фибоначчи: '))
res = [1, 1]
i = 2
while True:
    x = res[i-1] + res[i-2]
    i += 1
    if x > n: break
    else:
        res.append(x)
print(res)