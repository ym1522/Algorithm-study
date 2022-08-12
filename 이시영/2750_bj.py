from sys import stdin
m=[]
n= int(stdin.readline())
for _ in range(n):
    m.append(int(stdin.readline()))
m=sorted(m)

for i in m:
    print(i)