from sys import stdin

n, k = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
co = sum(a[:k])
temp = -10000
for i in range(k, n):
    co += a[i] - a[i-k]
    print(a[i], a[i-k])
    print(co)
    temp = max(temp, co)
    
print(temp)