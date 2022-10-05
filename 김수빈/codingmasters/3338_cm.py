import sys
N = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
D = {
     1: { 2: [2, 4, 5], 3: [3, 6, 7, 8, 9] },
     2: { 2: [1, 3, 4, 5, 6], 3: [7, 8, 9] },
     3: { 2: [2, 6, 5], 3: [1, 4, 7, 8, 9] },
     4: { 2: [1, 2, 5, 7, 8], 3: [3, 6, 9] },
     5: { 2: [1, 2, 3, 4, 6, 7, 8, 9], 3: [] },
     6: { 2: [2, 3, 5, 8, 9], 3: [1, 4, 7] },
     7: { 2: [4, 5, 8], 3: [1, 2, 3, 6, 9] },
     8: { 2: [4, 5, 6, 7, 9], 3: [1, 2, 3] },
     9: { 2: [5, 6, 8], 3: [1, 2, 3, 4, 7] },
}

cases = [1 for i in range(9)]

for t in times:
    if t == 1: continue
    
    new_cases = [0 for i in range(9)]
    for i in range(9):
        if cases[i] == 0: continue
        for j in D[i + 1][t]:
            new_cases[j - 1] += cases[i]
    cases = new_cases
    
print(sum(cases) % 1000000007)