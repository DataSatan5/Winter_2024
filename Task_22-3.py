import keyword

def replace_kw(text):
    kws = keyword.kwlist # Содержит перечень ключевых слов языка
    for kw in kws: # Циклом по перечню
        text = text.replace(kw, "<kw>")
    return text

text = input("Введите текст: ")
new_text = replace_kw(text) # Выполняюм замену слов в введенном тексте и получаем новый
print(new_text)