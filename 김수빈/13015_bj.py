def solution(n):
    max_len = (2 * n - 1) + 2 * (n - 1)
    stars = '*' + ' ' * (n - 2) + '*'

    rows = ['*' * n + ' ' * (max_len - 2 * n) + '*' * n]

    indices = list(range(1, n)) + list(range(n - 2, 0, -1))
    for i in indices:    
        if i == n - 1:
            rows += [' ' * i + stars + stars[1:]]
        else:
            spaces = ' ' * (max_len - 2 * i - 2 * len(stars))
            rows += [' ' * i + stars + spaces + stars] 

    rows += ['*' * n + ' ' * (max_len - 2 * n) + '*' * n]
    return rows

x = int(input())
print('\n'.join(solution(x)))