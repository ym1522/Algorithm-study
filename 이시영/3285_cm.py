from dis import dis
from sys import stdin
n=int(stdin.readline())
a,b=map(int,stdin.readline().split())
distance=[]
for _ in range(n):
    x,y=map(int,stdin.readline().split())
    distance.append((abs(a-x)+abs(b-y))*100)
print(min(distance))