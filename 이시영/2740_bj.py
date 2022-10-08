from sys import stdin

n, m=map(int,stdin.readline().split())
a = [list(map(int,(stdin.readline().split()))) for _ in range(n)]

m, k=map(int,stdin.readline().split())
b = [list(map(int,(stdin.readline().split()))) for _ in range(m)]

c = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            c[i][j]+=a[i][l]*b[l][j]
print("\n".join([' '.join([str(i) for i in row])for row in c]))