str1 = 'Предложение в котором несколько слов и совсем нету знаков препинания но оно подойдёт для задания'
mas = str1.split(' ')
maxlen = 1
for word in mas:
    if len(word) >= maxlen:
        maxlen = len(word)
        maxword = word
print(f"Самое длинное слово в предложении это - '{maxword}' и оно имеет длину {maxlen} знака(-ов)")