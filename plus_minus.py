import math
import os
import random
import re
import sys


def plusMinus(arr):
    # Write your code here
    total_elements = len(arr)
    pos = 0
    neg = 0
    non = 0
    for i in arr:
        if i>=1:
            pos += 1
        elif i ==0:
            non += 1
        elif i<1:
            neg += 1
        
    pos = round(pos/total_elements, 6)
    neg = round(neg/total_elements, 6)
    non = round(non/total_elements, 6)
    print(pos)
    print(neg)
    print(non)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
