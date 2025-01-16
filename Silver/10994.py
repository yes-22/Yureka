def star(x,y):
    s = ""
    num = 0
    for i in range(x):
        num = 1 - num
        s += "*" if num else " "
    for i in range(y+y-1):
        s += "*" if x%2==0 else " "
    for i in range(x):
        num = 1 - num
        s += " " if num else "*"
    s += "\n"
    return s

n = int(input())
n = (n*2)-1
result = ""
for i in range(n,0,-1): result += star(n-i,i)
for i in range(2,n+1,1): result += star(n-i,i)
print(result)