# 후보 추천하기
n = int(input())
re = int(input())
li = list(map(int, input().split()))
frames = {}
students = {}
for i in li:
    if i not in students:
        students[i] = 0
    elif i in students:
        students[i] += 1
        
    if len(frames) < n:
        frames[i] = 1
    elif len(frames) == n : 
        if i in frames:
            frames[i] += 1
        elif i not in frames:
            mins = [k for k,v in frames.items() if min(frames.values())==v]
            del frames[mins[0]]
            frames[i] = 1
sortFs = sorted(frames)
for i in range(n-1):
    print(sortFs[i],end=" ")
print(sortFs[-1])
