import sys
def solution(p, q):
    targets, divisor = [], []
    target = p * 10
    prefix = '0.'

    while True:
        if target == 0: break
        if targets and target in targets:
            idx = targets.index(target)
            return prefix + ''.join(divisor[:idx]) + '{' + ''.join(divisor[idx:]) + '}'
        
        d, r = target // q, target % q
        targets += [target]
        divisor += [str(d)]
        target = r * 10

    return prefix + ''.join(divisor)
    
p, q = map(int, sys.stdin.readline().split())
print(solution(p, q))