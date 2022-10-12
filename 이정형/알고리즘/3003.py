import sys

a = [1, 1, 2, 2, 2, 8]
b = list(map(int, sys.stdin.readline().split()))

result = [ai - bi for ai, bi in zip(a, b)]
for _ in result:
  print(_, end=' ')