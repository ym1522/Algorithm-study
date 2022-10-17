import sys

N, M = map(int, sys.stdin.readline().split())
coords = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

grid = coords[:N]
coords = coords[N:]

# 누적합 계산
for i in range(N):
    for j in range(N):
        upper_element = grid[i - 1][j] if i - 1 >= 0 else 0
        left_element = grid[i][j - 1] if j - 1 >= 0 else 0
        ul_element = grid[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0

        grid[i][j] += upper_element + left_element - ul_element

for x1, y1, x2, y2 in coords:
    common = grid[x1 - 2][y1 - 2] if x1 >= 2 and y1 >= 2 else 0
    b1 = grid[x1 - 2][y2 - 1] if x1 >= 2 else 0
    b2 = grid[x2 - 1][y1 - 2] if y1 >= 2 else 0

    print(grid[x2 - 1][y2 - 1] - b1 - b2 + common)