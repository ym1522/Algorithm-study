def solution(n):
    if n == 1: return ['*']

    prev = solution(n - 1)

    prev_max_len = max(list(map(len, prev)))
    max_len = 2 * (prev_max_len + 2) - 1
    iter_num = prev_max_len + 2

    prev_i = iter_num // 2
    rows = []
    # 짝수일 경우 -> 역삼각형
    if n % 2 == 0:
        rows += ['*' * max_len]
        for i in range(iter_num - 2, -1, -1):
            if i < prev_i:
                stars = '*' + ' ' * (2 * i - 1) + '*' if i > 0 else ' *'
            else:
                prev_stars = prev[prev_i - i - 1].lstrip()
                sub_spaces = ' ' * ((2 * i - 1 - len(prev_stars)) // 2)

                stars = '*' + sub_spaces + prev_stars + sub_spaces + '*'
            space_num = (max_len - len(stars)) // 2
            rows += [' ' * space_num + stars]
        
    # 홀수일 경우 -> 삼각형
    else:
        for i in range(iter_num - 1):
            if i < prev_i:
                stars = '*' + ' ' * (2 * i - 1) + '*' if i > 0 else '*'
            else:
                prev_stas = prev[i - prev_i].lstrip()
                sub_spaces = ' ' * ((2 * i - 1 - len(prev_stas)) // 2)

                stars = '*' + sub_spaces + prev_stas + sub_spaces + '*'
            space_num = (max_len - len(stars)) // 2
            rows += [' ' * space_num + stars]
        
        rows += ['*' * max_len]
    
    return rows

n = int(input())
print('\n'.join(solution(n)))