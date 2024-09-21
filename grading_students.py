import math
import os
import random
import re
import sys


def gradingStudents(grades):
    # Write your code here
    final_grades = []
    for i in grades:
        if i < 38:
            final_grades.append(i) 
        elif i % 5 == 0:
            final_grades.append(i)
        elif i % 5 != 0:
            diff = i % 5
            next_mul = 5 - diff
            if next_mul < 3:
                i = i + next_mul
            final_grades.append(i)
    return final_grades
            
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()