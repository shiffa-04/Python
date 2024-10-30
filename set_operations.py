n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())
operation = [input().split() for i in range(n_commands)]
for i in range(n_commands):
    if operation[i][0] == 'pop':
        s.pop()
    elif operation[i][0] == 'discard':
        s.discard(int(operation[i][1]))
    elif operation[i][0] == 'remove':
        value = int(operation[i][1])
        if value in s:
            s.remove(value)
        else:
            pass
            
print(sum(s))