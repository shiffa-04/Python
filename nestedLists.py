num_lis=[]

final_lis = []
for _ in range(int(input())):
    lis =[]
    name = input()
    score = float(input())
    lis.append(name)
    lis.append(score)
    final_lis.append(lis)
for student in final_lis:
    num_lis.append(student[1])
    
sortScore = sorted(set(num_lis))
second_lowest = sortScore[1]

name_Of_second_lowest=[]

for student in final_lis:
    if student[1] == second_lowest:
        name_Of_second_lowest.append(student[0])
        
name_sort = sorted(name_Of_second_lowest)
for i in name_sort:
    print(i)
