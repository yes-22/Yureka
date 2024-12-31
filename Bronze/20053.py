#첫 째줄에 테스트 케이스의 개수 입력 받기
#T개의 리스트 만들기
T = int(input())
#숫자를 저장할 리스트 생성성
N = []
#둘째 줄에는 N개의 정수를 공백으로 구분 -> split() 사용
for i in range(T):
    num = int(input())
    N.append(list(map(int, input().split())))
for i in range(T):
    print(min(N[i]),max(N[i]))
