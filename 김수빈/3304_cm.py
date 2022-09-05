import sys

S = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
inputs = list(map(lambda x: tuple(x.strip().split()), sys.stdin.readlines()))

for tgt, x, i in inputs:
    string = S[int(i):]
    S = S[:int(i)] + S[int(i):].replace(tgt, x, 1)
    print(S)
