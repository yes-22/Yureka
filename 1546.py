num = int(input())

score = list(map(int, input().split()))

max_score = max(score)

new = max_score / num * 100

print(new)