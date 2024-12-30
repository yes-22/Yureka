num = int(input())

score = list(map(int, input().split()))

max_score = max(score)

new_score = sum(score) / max_score * 100 / num

print(new_score)
