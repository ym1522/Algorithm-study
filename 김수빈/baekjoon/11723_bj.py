import sys

N = int(sys.stdin.readline())
S = [False for _ in range(21)]

for _ in range(N):
    inst = sys.stdin.readline().strip()
    inst = inst.split()
    if len(inst) == 1:
        if inst[0] == 'all':
            S = [True for _ in range(21)]
        elif inst[0] == 'empty':
            S = [False for _ in range(21)]
    else:
        x = int(inst[1])
        if inst[0] == 'add':
            S[x] = True
        elif inst[0] == 'remove':
            S[x] = False
        elif inst[0] == 'check':
            print(int(S[x]))
        elif inst[0] == 'toggle':
            S[x] = True if not S[x] else False