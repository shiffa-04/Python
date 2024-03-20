message=input("enter a message: ")
total=0
vowels=['a','e','i','o','u']
j=0
for i in message:
    for j in vowels:
        if i == j:
            total = total + 1
    j=+1

print(total)