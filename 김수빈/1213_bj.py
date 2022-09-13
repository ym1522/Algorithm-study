import sys

def solution(name, D):
    alpha = list(set(name))
    alpha.sort()

    left, mid, right = "", "", ""
    for x in alpha:
        while D[x] >= 2:
            left += x
            right = x + right
            D[x] -= 2
        if D[x] == 1 and not mid:
            mid = x
        elif D[x] == 1 and mid:
            return "I'm Sorry Hansoo"
    return left + mid + right

name = sys.stdin.readline().strip()
D = {}
for x in name:
    if not x in D: D[x] = 1
    else: D[x] += 1
print(solution(name, D))
