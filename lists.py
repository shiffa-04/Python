N = int(input())
n =[]
for i in range(N):
    cmd = input().split()
    if cmd[0] =='insert':
        n.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0]=='print':
        print(n)
    elif cmd[0]== 'remove':
        n.remove(int(cmd[1]))
    elif cmd[0]=='append':
        n.append(int(cmd[1]))
    elif cmd[0]=='sort':
        n.sort()
    elif cmd[0]=='pop':
        n.pop()
    elif cmd[0]=='reverse':
        n.reverse()
        
