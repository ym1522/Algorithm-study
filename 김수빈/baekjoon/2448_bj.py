from functools import reduce

n = int(input())

def solution(n):
    if n == 3: return ['  *  ', ' * * ', '*****']
    
    prev_unit = solution(n // 2)
    prev_len = len(prev_unit[0])
    max_len = prev_len * 2 + 1

    rows = []
    space_num = (max_len - prev_len) // 2
    rows += list(map(lambda x: ' ' * space_num + x + ' ' * space_num, prev_unit))
    rows += list(map(lambda x: x + ' ' + x, prev_unit))

    return rows

print('\n'.join(solution(n)))