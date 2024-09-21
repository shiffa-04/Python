import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple = 0
    orange = 0
    apples_dis = []
    oranges_dis = []
    for i in apples:
        i += a
        apples_dis.append(i)
    for i in oranges:
        i += b
        oranges_dis.append(i)
    
    for app in apples_dis:
        if app >= s and app <= t:
            apple+=1
    print(apple)       
    for ora in oranges_dis:
         if ora >= s and ora <= t:
            orange+=1
    print(orange)
       
            
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)