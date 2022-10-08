from sys import stdin

n,m = map(int,stdin.readline().split())
human=[0]*n
for i in range(m):
    a,b=map(int,stdin.readline().split())
    hu=list(map(int,stdin.readline().split()))
    for i in range(b):
        human[hu[i]-1]+=int(a/b)

result=" ".join(str(_) for _ in human)
print(result)