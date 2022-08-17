from sys import stdin
a,b,c=map(int,stdin.readline().split())

if a*a>b*b*c:
    print("NO")
else:
    print("YES")