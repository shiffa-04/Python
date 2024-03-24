import numpy

def arrays(arr):
    new_arr = numpy.array([])
    for i in range(len(arr)-1,-1,-1):
        new_arr = numpy.append(new_arr, arr[i])
    return(new_arr.astype(float))   
       
       

arr = input().strip().split(' ')
result = arrays(arr)
print(result)