n, m = input().split()
arr = list(map(int, input().split()))
element_in_A = set(map(int, input().split()))  
element_in_B = set(map(int, input().split()))

count = 0

for i in arr:
    if i in element_in_A:
        count += 1
    if i in element_in_B:
        count -= 1
print(count) 