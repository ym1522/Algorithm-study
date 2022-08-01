N = int(input())

def solution(N):
    min_cnt = None
    cases = [(0, N)]
    prev = []
    while cases:
        cnt, X = cases[0]
        cases = cases[1:]
        
        if X in prev: continue

        prev += [X]
        if X == 1:
            min_cnt = cnt if min_cnt is None or cnt < min_cnt else min_cnt
            continue

        if (min_cnt is not None and cnt >= min_cnt) or X <= 0: continue
        
        if X >= 3 and X % 3 == 0:
                cases += [(cnt + 1, X // 3)]
        if X % 2 == 0:
            cases += [(cnt + 1, X // 2)]

        cases += [(cnt + 1, X - 1)]
    
    return min_cnt

print(solution(N))