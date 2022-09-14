import sys

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10
    if a == 0:
        print(10)
    else:
        div = b % 4
        if div == 0:
            div += 4
        print((a**div) % 10)