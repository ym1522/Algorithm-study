import sys

def rsp(a, b, cnt1, cnt2):
    if a == 1:
        if b == 2:
            cnt2 += 1
        elif b ==3:
            cnt1 += 1
    elif a == 2:
        if b == 1:
            cnt1 += 1
        elif b == 3:
            cnt2 += 1
    elif a == 3:
        if b == 1:
            cnt2 += 1
        elif b ==2:
            cnt1 += 1
    return cnt1, cnt2

N = int(sys.stdin.readline())

cnt1 = 0
cnt2 = 0

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    cnt1, cnt2 = rsp(a, b, cnt1, cnt2)

print(cnt1, cnt2)