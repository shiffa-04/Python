from collections import Counter
no_of_shoes = int(input())
sizes = list(map(int, input().split(" ")))

availability = Counter(sizes)

# print(availability)

customers = int(input())

sum = 0

for i in range(0, customers):
    customer_sizes = list(map(int, input().split(" ")))
    if customer_sizes[0] in availability and availability[customer_sizes[0]] > 0:
        element_to_decrease = customer_sizes[0]
        availability[element_to_decrease] -= 1
        sum += customer_sizes[1]
print(sum)