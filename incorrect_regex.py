import re
x = int(input())
case = (input() for i in range(x))

for pattern in case:
    try:
        re.compile(pattern)  
        print(True)
    except re.error:
        print(False)