import sys

#입력 받을 개수 
num = int(input())
list_num = []

#num개의 숫자를 입력 받고 리스트에 저장
list_num = list(map(int, sys.stdin.read().split()))

#오름차순으로 정렬
list_num.sort()

#리스트 내용을 하나씩 출력
for i in list_num:
    print(i)