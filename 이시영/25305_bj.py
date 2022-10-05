from sys import stdin

n, k = map(int,stdin.readline().split())
a = list(map(int,input().split()))
a=sorted(a, reverse=True)
print(a[k-1])