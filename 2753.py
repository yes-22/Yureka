year = int(input())

#4의 배수이면서 100의 배수는 아니여야 함
#400의 배수는 ㄱㅊ
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(1) #" " 제외하고 작성해야함
else:
    print(0) 
