total_test_cases = int(input())
for i in range(total_test_cases):
    no_of_elements_A = int(input())
    elements_in_A = set(map(int, input().split()))
    
    no_of_elements_B = int(input())
    elements_in_B = set(map(int, input().split()))
    
    is_subset = True
    
    for j in elements_in_A:
        if j not in elements_in_B:
            is_subset = False
            break
    if is_subset:
        print("True")
    else:
        print("False")