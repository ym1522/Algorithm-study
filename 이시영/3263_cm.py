from sys import stdin
a,b=map(int,stdin.readline().split())

if (a%100)*0.04+4*(a//100)>=b:
    print("YES")
else:
    print("NO")