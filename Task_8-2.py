in_list = [[1, 5, 3], [2, 44, 1, 4], [3, 3]]
def sort_my(x):
    for lst in sorted(x, key = lambda x: len(x)):
        print(sorted(lst, reverse=True), end=', ')
sort_my(in_list)