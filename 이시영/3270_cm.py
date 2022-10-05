from sys import stdin

a, b=map(int,stdin.readline().split())
x, y=map(int,stdin.readline().split())
if (x-a)+(y-b)>=0 and x>=a:
    print("YES")
else:
    print("NO")