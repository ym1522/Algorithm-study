import sys
N = int(sys.stdin.readline())
cnt = 0

for B in range(1,501):
    for A in range(B,501):
        if A**2 == B**2 + N:
            cnt += 1
print(cnt)