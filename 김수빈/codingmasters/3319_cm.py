import sys

def solution(n, p, q):
    target = p * 10
    dec = ''
    for i in range(n + 1):
        d, r = target // q, target % q
        dec += str(d)
        target = r * 10

    dec = str(int(dec[:-1]) + 1) if int(dec[-1]) >= 5 else dec[:-1]
    return '0.' + dec

p, q = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
print(solution(n, p, q))