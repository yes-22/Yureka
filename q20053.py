# 최소, 최대 2
n = int(input())
a = []
for i in range(n):
    m = int(input())
    a.append(list(map(int, input().split())))
for i in range(n):
    print(min(a[i]),max(a[i]))