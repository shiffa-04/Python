from collections import OrderedDict
d = {}
number = int(input())
items = [input().rsplit(' ', 1) for _ in range(number)]
for item, price in items:
    price = int(price)
    if item in d:
        d[item] += price
    else:
        d[item] = price

for key, value in d.items():
    print(f"{key} {value}")