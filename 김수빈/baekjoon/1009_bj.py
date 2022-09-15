import sys

def solution(a, b):
    c = int(str(a)[-1])
    prev = []
    i = 0
    while not c in prev:
        prev += [c]
        c *= a
        c = int(str(c)[-1])
        i += 1
   
    result = prev[b % i - 1] 
    return result if result > 0 else 10

t = int(sys.stdin.readline())
cases = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))

for a, b in cases:
    print(solution(a, b))