from itertools import combinations

input_data = input().split()
string = input_data[0]
number = int(input_data[1])
sorted_data = sorted(string)
for i in range(0, number):
    comb = combinations(sorted_data, i+1)
    for c in comb:
        print("". join(c))
