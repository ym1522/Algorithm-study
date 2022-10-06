# 만약 '출력 형식이 잘못되었습니다.'가 뜨면 대체로 '\n'이 들어가 있기 때문에 틀렸다고 나옴
from sys import stdin

n = int(stdin.readline())

for i in range(n, 1, -1):
    print(' '*(n-i)+((i*2-1)*'*'))
for i in range(1, n+1):
    print(' '*(n-i)+((i*2-1)*'*'))