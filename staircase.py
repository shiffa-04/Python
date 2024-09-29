import math
import os
import random
import re
import sys

def staircase(n):
    # Write your code here
    for i in range(1, n+1):
        for j in range(n, 0, -1):
            if i<j:
                print(" ", end="")
            else:
                print("#", end="")
        print() 


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)