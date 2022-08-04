import sys

input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    
    ans = 0
    for _ in range(n):
        s = int(input())
        ans += s
    if ans == 0:
        print("0")
    elif ans > 0:
        print("+")
    else:
        print("-")