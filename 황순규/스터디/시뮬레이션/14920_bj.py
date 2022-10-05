import sys

num = int(sys.stdin.readline())

cnt = 1

while True:
    if num == 1:
        break
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
    cnt += 1

print(cnt)