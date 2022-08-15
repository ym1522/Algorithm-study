import sys

a, b = map(int, sys.stdin.readline().split())

sub = abs(a-b)

if sub > 30:
    print(60 - sub)
else:
    print(sub)