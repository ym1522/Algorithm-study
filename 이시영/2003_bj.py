# 투 포인터 알고리즘을 이용
from sys import stdin

n, m = map(int, stdin.readline().split())
a = list(map(int,stdin.readline().split()))

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += a[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= a[start]

print(count)
'''
# 완전 탐색은 시간복잡도가 O(N^2)이라서 시간초과가 남
from sys import stdin

n, m = map(int, stdin.readline().split())
a = list(map(int,stdin.readline().split()))
sum=0
count=0
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=a[j]
        if sum == m:
            count+=1
            break
        elif sum > m:
            break
print(count)
'''