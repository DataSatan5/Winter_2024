def camel_style(input_str):
    words = input_str.split() #перевод из строки в список
    camel_case = ''
    for word in words: #проход по словам во введенной строке
        camel_case += word.capitalize() #добавление в результирующий список слова с заглавной буквы
    return camel_case

input_str = "same lines goes wrong"
print(camel_style(input_str)) #SameStuffGoesWrong