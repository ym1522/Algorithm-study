from sys import stdin

n, k = map(int, stdin.readline().split())

coin = []
for i in range(n):
    coin.append(int(stdin.readline()))
count=0
for i in reversed(coin):
    count+=k//i
    k%=i
print(count)