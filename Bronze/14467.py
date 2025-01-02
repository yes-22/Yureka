#14467.py
N = int(input())
cow = {}
count = 0

for i in range(N):
    a, b =int(input().split())
    #해당 값이 없으면 딕셔너리에 추가
    if a not in cow:
        cow[a] = b
    #딕셔너리에 있을 경우 key 비교
    else:
        if cow[a] != b:
            count += 1
            #바뀐 b 값 업데이트
            cow[a] = b

print(count)