import math
import os
import random
import re
import sys


def breakingRecords(scores):
    # Write your code here
    score =0
    highest_score=0
    lowest_score = 0
    min_count = 0
    max_count = 0
    for i in range(0, len(scores)):
        score = scores[i]

        if i == 0:
            highest_score = score
            lowest_score = score

        if highest_score < score:
            highest_score = score
            max_count += 1

        if lowest_score > score:
            lowest_score = score
            min_count += 1

    return (max_count, min_count)
                
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()