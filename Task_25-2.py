def is_palindrome(str):
    s = str.lower().replace(" ", "")
    if len(s) <= 1:  # базовый случай: если строка пустая или состоит из одного символа
        return True
    elif s[0] != s[-1]:  # если первый и последний символы не совпадают
        return False
    else:
        return is_palindrome(s[1:-1])  # рекурсия: сравниваем "внутреннюю" часть строки

print(is_palindrome("TeNeT"))  # True
print(is_palindrome("hello world"))  # False