import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
num = []
for _ in range(5):
    num.extend(list(map(int, input().split())))

N = {}
for r in range(5):
    for c in range(5):
        N[board[r][c]] = (r, c)

def bingo(bd):
    count = 0
    
    for r in range(5):
        if all(x == 0 for x in bd[r]):
            count += 1
    for c in range(5):
        if all(bd[r][c] == 0 for r in range(5)):
            count += 1

    # 대각선 확인
    if all(bd[i][i] == 0 for i in range(5)):
        count += 1
    if all(bd[i][4 - i] == 0 for i in range(5)):
        count += 1

    return count

for i, number in enumerate(num):
    # 숫자의 위치를 찾아 0으로 변경경
    r, c = N[number]
    board[r][c] = 0

#빙고 체크
    if i >= 11:
       
        if bingo(board) >= 3:
            print(i + 1)  
            break
