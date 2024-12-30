#몇 개의 문자열을 입력 받을 것인지 작성
num = int(input())
total = 0

#입력받은 문자열을 리스트에 저장
for _ in range(num):
    s = input()
    string = list(s)
    count = 1

    #연속되지 않은 중복 발생 확인 
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i] in string[i + 1:]:
                count = 0
                break
    #중복 미발생 시 total 값에 1을 더함 
    if count == 1:
        total += 1


print(total)
