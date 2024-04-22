import math

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + math.floor((r - l) / 2)

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)  
        else:
            return binarySearch(arr, mid + 1, r, x)  

    else:
        return -1

arr = [1, 2, 5, 9, 23]  
l = 0
r = len(arr) - 1
q = 23  
print(binarySearch(arr, l, r, q))