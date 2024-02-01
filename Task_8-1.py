x = input("Введите строку из 'А', 'Г', 'Ц', 'Т' заглавными буквами: ")

def zamena(str):
    new_str = ""
    i = 0
    while i < len(str):
        if i < len(str) - 1 and (str[i] == "А" and str[i+1] == "Г" or str[i] == "Г" and str[i+1] == "А"):
            new_str += str[i+1] + str[i]
            i += 2
        elif i < len(str) - 1 and (str[i] == "Ц" and str[i+1] == "Т" or str[i] == "Т" and str[i+1] == "Ц"):
            new_str += str[i] + "АГ" + str[i+1]
            i += 2
        else:
            new_str += str[i]
            i += 1
    return new_str

print("Итоговая строка:", zamena(x))