import sys

K = int(sys.stdin.readline())

while True:
    K += 1
    if (K/2) % 2 == 1:
        print(K)
        break