import numpy

n, m, p = map(int, input().split(" "))
mat1 = numpy.array([list(map(int, input().split(" "))) for _ in range(n)])
mat2 = numpy.array([list(map(int, input().split(" "))) for _ in range(m)])

print(numpy.concatenate((mat1, mat2), axis = 0))