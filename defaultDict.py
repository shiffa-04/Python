n, m = map(int, input().split())
A = [input().strip() for _ in range(n)]
B = [input().strip() for _ in range(m)]

for word in B:
    re_list_1 = [str(i+1) for i in range(n) if A[i] == word]
    if re_list_1:
        print(" ".join(re_list_1))  
    else:
        print(-1)  