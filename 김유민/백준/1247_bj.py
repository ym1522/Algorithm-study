import sys

for _ in range(3):
    n = int(sys.stdin.readline())
    sum = 0
    for i in range(n):
        n = int(sys.stdin.readline())
        sum += n
    if sum == 0: print("0")
    elif sum > 0: print("+")
    elif sum < 0: print("-")