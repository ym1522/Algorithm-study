from functools import reduce

def solution(N):
    seqs = [['1']] + [[]] * (N - 1)

    for i in range(1, N):
        new_seq = []
        for j in range(max(i - 3, 0), i):
            k = i - j
            new_seq += list(map(lambda x: [x + f'{k}', f'{k}' + x ], seqs[j]))
        new_seq = reduce(lambda x, y: x + y, new_seq)
        new_seq = new_seq + [f'{i + 1}'] if i < 3 else new_seq
        
        seqs[i] = list(set(new_seq))
    return len(seqs[-1])

n = int(input())
for i in range(n):
    x = int(input())
    print(solution(x))