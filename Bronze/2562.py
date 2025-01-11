num = []

#9개의 수를 입력 받아서 리스트에 저장
for _ in range(9):
    number = int(input())
    num.append(number)

#max 함수 사용 
max_value = max(num)
max_index = num.index(max_value) + 1  

print(max_value)
print(max_index)