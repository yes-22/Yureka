# 스위치 켜고 끄기
import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
studentNum = int(sys.stdin.readline())
students = []
for i in range(studentNum):
    students.append(list(map(int,sys.stdin.readline().split())))
for std in students:
    if std[0] == 1:
        for i in range(len(a)):
            if (i+1)%std[1] == 0:
                if a[i] == 0:
                    a[i] = 1
                else: a[i] = 0
        #     print(a)
        # print("남자끝남",a)
    else:
        for i in range(1, len(a)):
            idx = std[1]-1
            if idx-i >=0 and idx+i <= len(a)-1:
                if a[idx-i] == a[idx+i]:
                    if a[idx-i] == 0:
                        a[idx-i] = a[idx+i] = 1
                    elif a[idx-i] == 1:
                        a[idx-i] = a[idx+i] = 0
                    # print(i, a)
                else: break
            else: break
        if a[idx] == 0:
            a[idx] = 1
        else: a[idx] = 0
        # print("여자끝남",a)
count=0
for i in range(n):
    print(a[i],end=" ")
    count+=1
    if count == 20:
        print()
        count = 0