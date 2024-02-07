with open('test1.txt', 'r', encoding='utf-8') as file1, open('test2.txt', 'w', encoding='utf-8') as file2:
    lines = file1.readlines() # Читаем содержимое первого файла
    lines.reverse()
    # print(lines)
    for line in lines: # Проходим по каждой строке
        words = line.split()
        # print(type(line), type(words))
        words.reverse() # Переворачиваем список слов
        file2.write(' '.join(words) + '\n') # Записываем перевернутую строку во второй файл
file1.close(), file2.close()