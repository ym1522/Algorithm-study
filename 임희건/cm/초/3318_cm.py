# 치훈이는 최근에 정수론 과목에서 친화수에 대해 배웠습니다.
# 두 양의 정수 A, B에 대하여, A의 진약수의 합이 B이고 B의 진약수의 합이 A라면 A와 B 쌍을 친화수 라고 합니다.
# (진약수란, 자기 자신을 제외한 약수를 말합니다.)
# 두 수의 쌍이 주어지면 친화수인지 판별하세요.

import sys

A, B = map(int, sys.stdin.readline().split())
a, b = [], []

for i in range(1, A // 2 + 1):
    if A % i == 0:
        a.append(int(i))
        
for j in range(1, B // 2 + 1):
    if B % j == 0:
        b.append(int(j))

if sum(a) == B and sum(b) == A:
    print('YES')
    
else:
    print('NO')