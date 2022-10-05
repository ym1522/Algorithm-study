import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

length = 0

if len(a) < len(b):
    S = a
    T = b
else:
    S = b
    T = a

ans = 0
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        temp = S[i:j]
        if temp in T:
            if ans < len(temp):
                ans = len(temp)
            print(len(temp))
        else:
            print(0)