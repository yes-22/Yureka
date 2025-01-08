# 지구온난화
import copy
size = list(map(int,input().split()))
li = []
[li.append(list(input())) for _ in range(size[0])]
coLi = copy.deepcopy(li)

seom = 0
for i in range(size[0]):
    seom+= li[i].count("X")
for i in range(size[0]):
    for k in range(size[1]):
        if li[i][k] == "X": 
            nearSea = 0
            
            if i == 0: nearSea += 1
            elif i-1 >=0:
                if li[i-1][k]==".": nearSea +=1

            if i == size[0]-1: nearSea += 1
            elif i+1 <=size[0]-1:
                if li[i+1][k]==".": nearSea +=1

            if k == 0: nearSea += 1
            elif k-1 >=0:
                if li[i][k-1]==".": nearSea +=1

            if k == size[1]-1: nearSea += 1
            elif k+1 <=size[1]-1:
                if li[i][k+1]==".": nearSea +=1
                
            if nearSea >= 3:
                coLi[i][k] = "."
                seom -= 1
        if seom == 1: break
    if seom == 1: break

rows=[]
cols=[]
for i in range(size[0]):
    if "X" in coLi[i]:
        rows.append(i)
    for k in range(size[1]):
        if coLi[i][k]=="X":
            if k not in cols:
                cols.append(k)
cols.sort()
for i in range(rows[0], rows[-1]+1):
    for k in range(cols[0], cols[-1]+1):
        print(coLi[i][k],end="")
    print()