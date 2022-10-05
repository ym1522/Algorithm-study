import sys
n = int(sys.stdin.readline())
i, tmp = 0, 0

while tmp+1 < n:
    i += 1; tmp += 6*i
print(i+1)