import sys

size = int(sys.stdin.readline().strip())
maps = []

for i in range(size):
    a = list(map(int, sys.stdin.readline().split()))
    if 1 in a:
        maps.append(a)
    else:
        maps.append([0]*size)
        
result = 0
for i in range(size):
    rice = False
    f = 0
    for j in range(size):
        if maps[j][i] == 1:
            rice = True
        elif maps[j][i] == 2:
            f += 1
    if not rice:
        continue
    else:
        result += f
        
print(result)