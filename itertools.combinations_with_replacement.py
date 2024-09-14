from itertools import combinations_with_replacement

data = input().split()
string = data[0]
number = int(data[1])
sorted_data = sorted(string)
comb = combinations_with_replacement(sorted_data, number)
for c in comb:
    print(''.join(c))
