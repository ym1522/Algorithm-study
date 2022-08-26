import sys

c = int(sys.stdin.readline())
k = 1
while c != 1:
    if c % 2 == 0:
        c /= 2
    else:
        c = 3 * c + 1
    k += 1
print(k)