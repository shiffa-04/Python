elements_of_A = set(map(int, input().split()))
no_of_sets = int(input())

strict_superset = True
for i in range(no_of_sets):
    other_set = set(map(int, input().split()))
    for i in other_set:
        if i not in elements_of_A:
            strict_superset = False
            break
            
if strict_superset:
    print("True")
else:
    print("False")