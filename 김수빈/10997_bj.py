def solution(x):
    if x == 1: return ['*']
    n = 4 * (x - 1) + 1
    prev = solution(x - 1)

    rows = []
    rows += ['*' * n, '*']

    if len(prev) == 1:
        prev = prev * 3 
    
    star_num = n - 2 - len(prev[0])
    rows += ['* ' + prev[0] + '*' * star_num]
    for line in prev[1:]:
        space_num = n - 3 - len(line)
        rows += ['* ' + line + ' ' * space_num + '*']
    
    rows += ['*' + ' ' * (n - 2) + '*']
    rows += ['*' * n]
    return rows

x = int(input())
print('\n'.join(solution(x)))