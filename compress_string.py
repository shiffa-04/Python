from itertools import groupby

data = input()

for key, group in groupby(data):
    occ = 0
    for i in group:
        occ += 1
    result = (occ, int(key))
    print(result, end=" ")

