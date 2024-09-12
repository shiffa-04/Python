from itertools import permutations

inputString = input().split()
var = inputString[0]
length = int(inputString[1])
per_data = permutations(list(var), length)
sorted_data= sorted(per_data)
for i in sorted_data:
    print(''.join(i))

