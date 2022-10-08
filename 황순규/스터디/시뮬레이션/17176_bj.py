import sys
# import numpy as np

N = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))
answer = list(sys.stdin.readline().strip())
P = []
for i in answer:
    if i == ' ':
        P.append(0)
    elif i.isupper():
        P.append(ord(i) - ord('A') + 1)
    else:
        P.append(ord(i) - ord('a') + 27)
C.sort()
P.sort()

flag = True
for i in range(N):
    if P[i] - C[i] != 0:
        flag = False

if flag:
    print('y')
else:
    print('n')

