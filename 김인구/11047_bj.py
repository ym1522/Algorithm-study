n, k = map(int, input().split())
coin = []
for _ in range(n):
     coin.append(int(input()))

coin.sort(reverse=True)

result = 0
for i in range(n):
    result += k // coin[i]
    k = k % coin[i]
print(result)