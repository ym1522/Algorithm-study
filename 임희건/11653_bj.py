import sys

N = int(sys.stdin.readline())

if N > 1:
    n = 2

    while n <= N:
        if N % n == 0:
            print(n)
            N = N / n

        else:
            n = n + 1