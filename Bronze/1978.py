#1978번

n = int(input())
num_list = list(map(int, input().split()))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime(num_list):
    prime_count = 0
    for num in num_list:
        if is_prime(num):
            prime_count += 1
    return prime_count

count = count_prime(num_list)
print(count)