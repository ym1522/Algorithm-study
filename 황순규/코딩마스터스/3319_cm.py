import sys

p, q = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
answer = '0.'
for i in range(N): 
    d = str(p/q).split('.')[1][0]
    answer += d
    p -= float(answer) * q
    print(p)
print(answer)

#### 아직 못풂