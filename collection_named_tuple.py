from collections import namedtuple

N = int(input())

columns = input().split()

data = [input().split() for i in range(N)]

student = namedtuple('student', columns)

students = [student(*d) for d in data]
sum = 0
for student in students:
    sum += int(student.MARKS)
print(sum/N)