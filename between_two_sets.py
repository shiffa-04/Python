import math
import os
import random
import re
import sys

def find_lcm(a):
    l = a[0]
    for i in range(1, len(a)):
        l = math.lcm(l, a[i])
    return l
    
def find_gcd(b):
    m = b[0]
    for i in range(1, len(b)):
        m = math.gcd(m, b[i])
    return m

def find_multiples(l, m):
    counting = 0
    multiple = l
    while multiple <= m:
        if m % multiple == 0:
            counting += 1
        multiple += l
    return counting
    
def getTotalX(a, b):
    # Write your code here
    lcm_of_a = find_lcm(a)
    gcd_of_b = find_gcd(b)
    total_numbers = find_multiples(lcm_of_a, gcd_of_b)
    return total_numbers
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()