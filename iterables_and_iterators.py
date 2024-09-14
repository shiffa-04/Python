from itertools import combinations

length = int(input())
data = input().split(" ")
indicies = int(input())

# print(length, data, indicies)

index_of_a = []
for i in range(0, len(data)):
    if data[i] == "a":
        index_of_a.append(i+1)
index_of_a = tuple(index_of_a)
# print(index_of_a)

for i in range(0, len(data)):
    data[i] = i+1
# print(data)

comb = combinations(data, indicies)
comb_list = list(comb)
# print(comb_list)

sum = 0
for i in comb_list:
    # print(i)
    for j in index_of_a:
        # print(j)
        if j in i:
            sum += 1
            break
# print(sum)

prob = round(sum/len(comb_list), 4)
print(prob)
