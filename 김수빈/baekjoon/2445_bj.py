n = int(input())
max_star = 2 * n

indices = list(range(1, n)) + list(range(n, 0, -1))
for i in indices:
    space_num = max_star - 2 *i
    print('*' * i + ' ' * space_num + '*' * i)
