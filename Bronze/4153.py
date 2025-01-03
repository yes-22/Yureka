#4153.py

a, b, c = input().split()

while a != 0:
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("right")
    else:
        print("wrong")
