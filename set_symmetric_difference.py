s1_size = int(input())
set1 = set(input().split())
s2_size = int(input())
set2 = set(input().split())

diff_1 = set1.difference(set2)
diff_2 = set2.difference(set1)

diff_1.update(diff_2)
symmetric_diff = list(map(int, diff_1))
sor_symm_diff = sorted(symmetric_diff)
for i in sor_symm_diff:
    print(i)