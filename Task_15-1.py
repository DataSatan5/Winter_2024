def get_vals(d, x):
    res = []
    for key, value in d.items():
        if key == x:
            res.append(value)
        elif type(value) == dict:
            res.extend(get_vals(value, x))
    return res

dct = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11}, 6:22}
x = 1
print(get_vals(dct, x))