import itertools
banknotes = [10, 50, 100, 200, 500, 1000, 2000, 5000]
sums = set()

for j in range(1, len(banknotes)+1):
    for i in itertools.combinations(banknotes, j):
        sums.add(sum(i))

print(*sorted(sums))