numA = int(input())
list_of_A = set(map(int, input().split()))
num_other = int(input())

for i in range(num_other):
    name, size = input().split()
    size = int(size)
    
    other_set = set(map(int, input().split()))
    
    if name == "intersection_update":
        list_of_A.intersection_update(other_set)
    elif name == "update":
        list_of_A.update(other_set)
    elif name =="difference_update":
        list_of_A.difference_update(other_set)
    elif name == "symmetric_difference_update":
        list_of_A.symmetric_difference_update(other_set)
print(sum(list_of_A))