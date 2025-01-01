# ZOAC 3
start = list(input().split())
word = list(input())
size = len(word)
jaeum = [list("qwert"),
         list("asdfg"),
         list("zxcv")]
moeum = [list("yuiop"),
         list("hjkl"),
         list("bnm")]
left = []
right = []

for i in range(len(start)):
    for k in range(3):
        if start[i] in jaeum[k]:
            left.append([k,jaeum[k].index(start[i])])
    for j in range(3):
        if start[i] in moeum[j]:
            right.append([j,moeum[j].index(start[i])])

leftFlag = 1
rightFlag = 1
for i in range(size):
    if leftFlag == 1 and word[i] in start:
        leftFlag = 0
        continue
    if rightFlag == 1 and word[i] in start:
        rightFlag = 0
        continue
    for k in range(3):
        if word[i] in jaeum[k]: 
            left.append([k, jaeum[k].index(word[i])])
    for j in range(3):
        if word[i] in moeum[j]:
            right.append([j, moeum[j].index(word[i])])
            
timeCnt=0
for i in range(len(left)-1):
    timeCnt += abs(left[i][0]-left[i+1][0])
    timeCnt += abs(left[i][1]-left[i+1][1])

for i in range(len(right)-1):
    timeCnt += abs(right[i][0]-right[i+1][0])
    timeCnt += abs(right[i][1]-right[i+1][1])
timeCnt += len(word)
print(timeCnt)