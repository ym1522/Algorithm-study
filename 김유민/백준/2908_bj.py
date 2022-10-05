import sys

a, b = sys.stdin.readline().rstrip().split(' ')
a, b = int(a[::-1]), int(b[::-1])

print(a if a>b else b)  # max()보다 빠름