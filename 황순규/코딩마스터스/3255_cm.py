import sys

N, M = map(int, sys.stdin.readline().split())

colors_dict = {'RR':'R', 'GG':'G', 'BB':'B', 'RG':'Y', 'GR':'Y',
               'GB':'C', 'BG':'C', 'BR':'M', 'RB':'M'}

colors = []
for i in range(N):
    colors.append(list(sys.stdin.readline().split()))

for i in range(N):
    colors2 = list((sys.stdin.readline().split()))
    for j in range(M):
        colors[i][j] += colors2[j]
        colors[i][j] = colors_dict[colors[i][j]]

for i in range(N):
    for j in range(M):
        print(colors[i][j], end= ' ')
    print()