mas = []
counter = 1
while True:
    zp = int(input(f'Введите зарплату {counter} сотрудника: '))
    counter += 1
    if zp == 0:
        break
    else: mas.append(zp)
sr_zp = sum(mas) / len(mas)
print()
print(f'Средняя ЗП на предприятии равна {sr_zp}')