# 입력 받기
S = input()

# 알파벳 리스트
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# 저장할 리스트 
positions = [-1] * 26

# 각 알파벳의 처음 등장 위치 찾기
for index, char in enumerate(S):
    if positions[ord(char) - ord('a')] == -1:
        positions[ord(char) - ord('a')] = index

print(' '.join(map(str, positions)))