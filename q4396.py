# 지뢰 찾기

n = int(input())

bombs=[]
[bombs.append(list(input())) for _ in range(n)]
opened = []
[opened.append(list(input())) for _ in range(n)]

bombCnt = [[0 for j in range(n)] for i in range(n)]

# bombCnt 구성
for i in range(n):
    for k in range(n):
        if bombs[i][k] == "*":
            if i-1>=0:
                if k-1>=0: bombCnt[i-1][k-1] += 1
                bombCnt[i-1][k] += 1
                if k+1<=n-1: bombCnt[i-1][k+1] += 1
            if k-1>=0: bombCnt[i][k-1] += 1
            bombCnt[i][k] += 1
            if k+1<=n-1: bombCnt[i][k+1] += 1
            if i+1<=n-1:
                if k-1>=0: bombCnt[i+1][k-1] += 1
                bombCnt[i+1][k] += 1
                if k+1<=n-1: bombCnt[i+1][k+1] += 1
    # print(i,"행 ", k,"열")
    # print(bombCnt[i])
    # print()

flag = 0
for i in range(n):
    for k in range(n):
        if flag == 0:
            if opened[i][k] == ".":
                bombCnt[i][k] = "."
            elif opened[i][k] == "x" and bombs[i][k] == "*":
                flag = 1
        if flag == 1: break
    if flag == 1: break
          
if flag == 1 :
    for i in range(n):
        for k in range(n):
            if bombs[i][k] == ".": bombCnt[i][k] = "."
            if bombs[i][k] == "*": bombCnt[i][k] = "*"
for i in range(n):
    for k in range(n):
        print(bombCnt[i][k],end="")
    print()