def combo(lst):
    import itertools
    res = []
    for i in itertools.permutations(lst):
        #xx = ''.join(map(str, i))
        res.append(int(''.join(map(str, i))))
        #print(res)
        outp = sorted(res, reverse=True)[0]
    return outp

lst1 = ['1', '23', '45']
lst2 = [98, 4, 10]
lst3 = [9, 99, 68, 10, 33]

print(combo(lst1))
print(combo(lst2))
print(combo(lst3))