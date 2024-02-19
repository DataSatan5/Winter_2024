import re
alf = 'ABCEHKMOPTXYАВСЕНКМОРТХУ'
regex = fr"[{alf}]\d\d\d[{alf}][{alf}]1?78"
string = input()
print(re.findall(regex, string))