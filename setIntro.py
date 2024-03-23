def average(array):
    a = set(array)
    arr_sum = sum(a)
    length = len(a)
    average = arr_sum/length
    return average
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)