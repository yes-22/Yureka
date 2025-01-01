# 빙고
nums = []
[nums.append(list(map(int, input().split()))) for _ in range(5)]
bingo = []
[bingo.append(list(map(int, input().split()))) for _ in range(5)]
output = [[0 for k in range(5)] for i in range(5)]
numCnt = 0
flag = 0
   
def isBingo(output, numCnt):
    bingoCnt = 0
    for i in range(5):
        if output[i][0] == output[i][1] == output[i][2] == output[i][3] == output[i][4] == 1 :
            bingoCnt += 1
    for k in range(5):
        if output[0][k] == output[1][k] == output[2][k] == output[3][k] == output[4][k] == 1:
            bingoCnt += 1
    if output[0][0] == output[1][1] == output[2][2] == output[3][3] == output[4][4] == 1:
        bingoCnt += 1
    if output[4][0] == output[3][1] == output[2][2] == output[1][3] == output[0][4] == 1:
        bingoCnt += 1
    if bingoCnt >= 3: 
        return True
    else: return False

for q in range(5): 
    for w in range(5): 
        for i in range(5):
            for k in range(5):
                if nums[i][k] == bingo[q][w]: 
                    output[i][k] = 1
                    numCnt += 1
                    if(isBingo(output, numCnt)):
                        print(numCnt)
                        flag = 1
                if flag == 1: break
            if flag == 1: break
        if flag == 1: break
    if flag == 1: break