from collections import deque

n = int(input())
operations = [input().split() for i in range(n)]

d = deque()

for i in range(n):
    if operations[i][0] == "append":
        d.append(operations[i][1])
    elif operations[i][0] == "appendleft":
        d.appendleft(operations[i][1])
    elif operations[i][0] == "pop":
        d.pop()
    elif operations[i][0] == "popleft":
        d.popleft()
for i in d:
    print(i, end = " ")