from sys import stdin
a,b,c=map(int,stdin.readline().split())
if max(a,b,c)==a:
    print(int(b*c/2))
elif max(a,b,c)==b:
    print(int(a*c/2))
else:
    print(int(a*b/2))