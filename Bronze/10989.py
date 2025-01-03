#10989.py
import sys


n = int(input())
num_list = [0 for i in range(10001)]

for i in range(n):
    num_list[n] += 1
    
for i in range(len(num_list)):
    for j in range(num_list[i]):
        print(i)