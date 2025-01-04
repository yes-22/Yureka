# 소가 길을 건너간 이유 1
n = int(input())
cows = []
[cows.append(list(map(int, input().split()))) for _ in range(n)]
cowDone = []
count = 0
for i in range(0,n-1):
    cowNum = cows[i][0]
    cowLoc = cows[i][1]
    if cowNum in cowDone: continue
    for k in range(i+1, n):
        nextCowNum = cows[k][0]
        nextCowLoc = cows[k][1]
        if nextCowNum == cowNum:
            if nextCowLoc != cowLoc: 
                cowLoc = nextCowLoc
                count += 1
    cowDone.append(cowNum)
print(count)