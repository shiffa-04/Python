group_size = int(input())
room_no = map(int,input().split())

d={}
for i in room_no:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

for key, value in d.items():
    if value == 1:
        print(key)