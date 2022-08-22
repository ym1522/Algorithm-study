import sys

N = int(sys.stdin.readline())
count = 0
for i in range(1, 501):
    j = 1
    while j <= i:
        if i ** 2 - j ** 2 == N:
            count += 1
        j += 1
print(count)