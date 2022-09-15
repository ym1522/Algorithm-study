import sys

N = int(sys.stdin.readline())
cls_room = sys.stdin.readline().strip()
wind = [1] + [0] * N + [1]
for i in range(1, N + 1):
    if cls_room[i - 1] == 'X': 
        if wind[i + 1] >= 0: wind[i + 1] += 1
        wind[i] = -1
        if wind[i - 1] >= 0: wind[i - 1] += 1

cnt = cls_room.count("X")
for i in range(1, N + 1):
    if wind[i] < 0 and (wind[i - 1] < 0 or wind[i - 1] > 1) and (wind[i + 1] < 0 or wind[i + 1] > 1):
        cnt -= 1
        if wind[i - 1] > 0: wind[i - 1] -= 1
        if wind[i + 1] > 0: wind[i + 1] -= 1
print(cnt)