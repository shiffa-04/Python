import numpy as np

n, m = map(int, input().split(" "))
arr = np.array([list(map(int, input().split(" ")))for _ in range(m)])

arr_sum = np.sum(arr, axis=0)
print(np.prod(arr_sum))