n = int(input())
unit = ['***', '* *', '***']

def solution(n):
    if n == 3: return unit
    
    prev_unit = solution(n // 3)
    unit_len = len(prev_unit[0])

    result = []
    for i in range(3):
        if i == 1:
            rows = list(map(lambda x: x + ' ' * unit_len + x, prev_unit))
        else:
            rows = list(map(lambda x: x * 3, prev_unit))
        result += rows

    return result

print('\n'.join(solution(n)))