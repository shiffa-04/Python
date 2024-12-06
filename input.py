x, k = map(int, input().split())  
polynomial = input().strip()     


result = eval(polynomial)
print(result == k)
