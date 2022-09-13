import sys

N = int(sys.stdin.readline())
a = N
count = 0

while True:
    b = a // 10 + a % 10
    new_N = a % 10 * 10 + b % 10
    count += 1

    if new_N == N:
        break

    else:
        a = new_N

print(count)