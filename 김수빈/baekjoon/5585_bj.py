import sys

cost = int(sys.stdin.readline())
left = 1000 - cost
cnt = 0
while left:
    if left >= 500:
        left -= 500
    elif left >= 100:
        left -= 100
    elif left >= 50:
        left -= 50
    elif left >= 10:
        left -= 10
    elif left >= 5:
        left -= 5
    else:
        left -= 1
    cnt += 1
print(cnt)