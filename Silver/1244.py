N = int(input())
switch = [-1] + list(map(int, input().split()))
student = int(input())

for _ in range(student):
    gender, num = map(int, input().split())
    # 남학생
    if gender == 1:
        for i in range(num, N + 1, num):
            switch[i] = 1 - switch[i]

    # 여학생
    elif gender == 2:
        switch[num] = 1 - switch[num]
        for j in range(1, min(num, N - num + 1)):
            if switch[num - j] == switch[num + j]:
                switch[num - j] = 1 - switch[num - j]
                switch[num + j] = 1 - switch[num + j]
            else:
                break

for i in range(1, N + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()