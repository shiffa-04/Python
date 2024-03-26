import numpy as np


rows, columns = map(int, input().split(" "))
mat = np.array([list(map(int, input().split(" ")))for _ in range(rows)])
      
transpose = mat.T
print(transpose.astype(int))
print(mat.ravel().astype(int))