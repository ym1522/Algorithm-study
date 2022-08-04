def solution(n):
    if n == 1: return ['*']
    prev = solution(n - 1)
    prev_m = len(prev[0])
    m = prev_m + 4
    
    rows = []
    for i in range(1, m + 1):
        if i == 1 or i == m: rows += ['*' * m]
        
        elif i == 2 or i == m - 1:
            rows += ['*' + ' ' * (m - 2) + '*']
        else:
            rows += ['* '+ prev[i - 3] + ' *']
    
    return rows

n = int(input())
print('\n'.join(solution(n)))