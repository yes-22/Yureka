#학생들 리스트 제작
student = []

#1번부터 30번까지 추가
for i in range(1, 31):
    student.append(i)

#입력받은 28개의 수 삭제
for i in range(28):
    student.remove(int(input()))

# 오름차순 정렬
student.sort()

#리스트에 남아있는 0번과 1번 출력
print(student[0])
print(student[1])
