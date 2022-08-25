import sys
import copy

N = int(sys.stdin.readline())

bat = []

for i in range(N):
    bat.append(list(sys.stdin.readline().split()))
bat1 = copy.deepcopy(bat)
min1 = N**2
max2 = 0
for i in range(N):
    for j in range(N):
        count1 = 0
        for k in range(N):
            if bat[(i+k)%N][j] == "1":
                count1 += 1
            if bat[i][(j+k)%N] == "1":
                count1 += 1
        if bat[i][j] == '1':
            count1 -= 1
        bat1[i][j] = count1
        if min1 > count1:
            min1 = count1
print(bat1)
print(bat)

# for i in range(N):
#     for j in range(N):


## 아직 못풂