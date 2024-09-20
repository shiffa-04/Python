import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    # Write your code here
    minimum = 0
    maximum = 0
    
    length = len(arr)
    arr = sorted(arr)
    
    for i in range(0, length - 1):
        minimum += arr[i]
    
    for j in range(length - 1, 0, -1):
        maximum += arr[j]
    
    print(f"{minimum} {maximum}")
        
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
