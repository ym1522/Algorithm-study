from functools import reduce

def solution(N, k):
    seqs = [['1']] + [[]] * (N - 1)

    for i in range(1, N):
        new_seq = []
        for j in range(max(i - 3, 0), i):
            m = i - j
            new_seq += list(map(lambda x: [x + f'{m}', f'{m}' + x ], seqs[j]))
        new_seq = reduce(lambda x, y: x + y, new_seq)
        new_seq = new_seq + [f'{i + 1}'] if i < 3 else new_seq
        
        seqs[i] = list(set(new_seq))
    answer = seqs[-1]
    answer.sort()
    if k > len(answer) : return -1
    return '+'.join(list(answer[k-1]))

N, k = map(int, input().split())
print(solution(N, k))