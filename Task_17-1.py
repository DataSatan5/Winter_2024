import re
mytext = 'Напишите программу программу, которая устраняет повторение повторение слов, т.е. результат результат должен быть следующим.'
def noDuplicates(mytext):
    slova = re.split(r"\, |\ |\. |\.|\n", mytext)
    res = []
    #print(slova)
    for s in slova:
        if s not in res:
            res.append(s)
            print(res)
        else:
            pass
    return '_'.join(res)
    #print(res)

fin = noDuplicates(mytext)
print(fin)