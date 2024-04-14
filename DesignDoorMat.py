n, m = map(int, input().split(" "))

#upper-part:

middle_segment = ".|."
for i in range(1, n, 2):
    left_dash_count = (m - len(middle_segment) * i) // 2
    right_dash_count = left_dash_count
    print("-" * left_dash_count + ".|."*i + "-"*left_dash_count)
    
#middle-part:

print("-"*((m-7)//2)+"WELCOME"+"-"*((m-7)//2))

#lower-part:

middle_segment = ".|."
for i in range(n-2, 0, -2):
    left_dash_count = (m - len(middle_segment) * i) // 2
    right_dash_count = left_dash_count
    print("-"* left_dash_count + ".|."*i + "-"*left_dash_count)
