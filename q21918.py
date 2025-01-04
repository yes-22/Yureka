# 전구
n, m = input().split()
n = int(n)
m = int(m)
bulbs = list(map(int, input().split()))
li = []
[li.append(list(map(int, input().split()))) for _ in range(m)]
for i in range(m):
    a = li[i][0]
    b = li[i][1]
    c = li[i][2]
    if a == 1:
        bulbs[b-1] = c
    elif a == 2:
        for j in range(b-1, c):
            bulbs[j] = 0 if bulbs[j] == 1 else 1
    elif a == 3:
        for j in range(b-1, c):
            bulbs[j] = 0
    elif a == 4:
        for j in range(b-1, c):
            bulbs[j] = 1
[print(bulbs[i], end=" ") for i in range(len(bulbs))]