#10989.py
import sys
input = sys.stdin.read

n = int(input().splitlines()[0])
num_list = [0] * 10001 

data = input().splitlines()[1:] 
for num in data:
    num_list[int(num)] += 1 
    
for i in range(10001):
    if num_list[i] > 0:
        sys.stdout.write(f"{i}\n" * num_list[i]) 
