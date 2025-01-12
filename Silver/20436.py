left = {'q': (1, 1), 'w': (2, 1), 'e': (3, 1), 'r': (4, 1), 't': (5, 1),
             'a': (1, 2), 's': (2, 2), 'd': (3, 2), 'f': (4, 2), 'g': (5, 2),
             'z': (1, 3), 'x': (2, 3), 'c': (3, 3), 'v': (4, 3), }

right = {'y': (1, 1), 'u': (2, 1), 'i': (3, 1), 'o': (4, 1), 'p': (5, 1),
              'h': (1, 2), 'j': (2, 2), 'k': (3, 2), 'l': (4, 2),
              'b': (0, 3), 'n': (1, 3), 'm': (2, 3)}

l_start, r_start = input().split()
num = input()
time = 0

for i in num:
    if i in left:
        time += abs(left[l_start][0] - left[i][0])
        time += abs(left[l_start][1] - left[i][1])
        l_start = i
        time += 1
    if i in right:
        time += abs(right[r_start][0] - right[i][0])
        time += abs(right[r_start][1] - right[i][1])
        r_start = i
        time += 1

print(time)