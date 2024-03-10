n = int(input())
arr = map(int, input().split())
winner =-120
runnerUp=-120
for i in arr:
    if i > winner:
        runnerUp = winner
        winner = i
    elif i < winner and i > runnerUp:
        runnerUp = i
print(runnerUp)