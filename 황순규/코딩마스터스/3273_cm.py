import sys
N = int(sys.stdin.readline())

while N != 1:
    print(N, end = " ")
    if N % 2 == 0:
        N = N//2
    else:
        N = N * 3 + 1
print(N, end = " ")