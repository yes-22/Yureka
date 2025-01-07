# 지구온난화
size = list(map(int,input().split()))
li = []
[li.append(list(input())) for _ in range(size[0])]
seom = 0
for i in range(size[0]):
    seom+= li[i].count("X")
for i in range(size[0]):
    for k in range(size[1]):
        if li[i][k] == "X": 
            nearSea = 0
            if i == 0: nearSea += 1
            elif i-1 >=0:
                if li[i-1]==".": nearSea +=1
            if i == size[0]-1: nearSea += 1
            elif i+1 <=size[0]-1:
                if li[i-1]: nearSea +=1
                
                
            if nearSea >= 3:
                li[i][k] = "."
                seom -= 1
        
        if seom == 1: break
    if seom == 1: break