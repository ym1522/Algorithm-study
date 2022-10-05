from sys import stdin

n = int(stdin.readline())

a = list(map(int,stdin.readline().split()))
b = list(map(int,stdin.readline().split()))

sum=0
for i in range(n):
    sum += min(a)*max(b)
    a.pop(a.index(min(a)) )
    b.pop(b.index(max(b)))
print(sum)