import sys

T = int(sys.stdin.readline())
testcase = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))

def solution(h, w, n):
    no = (n - 1) // h + 1
    floor = n % h
    floor = floor if floor > 0 else h

    return str(floor) + "%02d" % no

for h, w, n in testcase:
    print(solution(h, w, n))