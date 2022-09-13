import sys

coms = int(sys.stdin.readline())
N = int(sys.stdin.readline())

all_coms = []
vir = []
n_vir = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    all_coms.append((min(a,b), max(a,b)))
    
all_coms.sort(key = lambda x:x[0])

vir.append(all_coms[0][0])
vir.append(all_coms[0][1])

for i in all_coms[1:]:
    if i[0] in vir:
        vir.append(i[1])
    else:
        n_vir.append(i[1])
        
if all_coms[0][0] == 1:
    print(N + 1)
else:
    print(len(set(vir)) - 1)