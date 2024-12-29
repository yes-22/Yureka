#입력 받을 개수 
num = int(input())
list_num = []

#num개의 숫자를 입력 받고 리스트에 저장
for _ in range(num):
    s = int(input())
    list_num.append(s)

#오름차순으로 정렬
list_num.sort()

#리스트 내용을 하나씩 출력
for i in list_num:
    print(i)