n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

sum=0

if student_marks[query_name]:
    lis_Of_marks = student_marks[query_name]

for i in lis_Of_marks:
    sum = sum + i
    
result = sum / len(lis_Of_marks)
result= "{:.2f}".format(result)
print(result)