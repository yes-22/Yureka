# 과제 안 내신 분..?
a = []
for i in range(1,31):
    a.append(i)
for i in range(28):
    a.remove(int(input()))
a.sort()
print(a[0])
print(a[1])