#split()을 이용해 띄어쓰기를 기준으로 입력 받기기
N, M = map(int,input().split())
bulb_list = list(map(int, input().split()))

#함수 선언 
def cmd(a, b, c) :
    if a == 1 :
        bulb_list[b-1] = c
    elif a == 2 :
        for i in range(b-1, c):
            if bulb_list[i] == 0 :
                bulb_list[i] = 1
            else :
                bulb_list[i] = 0
    elif a == 3 :
        for i in range(b-1, c):
            bulb_list[i] = 0
    elif a == 4 :
        for i in range(b-1, c):
            bulb_list[i] = 1

#a,b,c를 묶는 cmd 정의를 안해줬단걸 이제 알았어유...
for _ in range(M):
    a, b, c = map(int, input().split()) 
    cmd(a, b, c)

#리스트 출력 
for i in bulb_list:
    print(i, end=' ')
