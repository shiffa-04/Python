stu_eng = int(input())
eng_students = set(input().split())
stu_fre = int(input())
fre_students = set(input().split())

subscribed_both = eng_students.intersection(fre_students)
print(len(subscribed_both))