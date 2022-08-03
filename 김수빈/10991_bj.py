n = int(input())
max_len = 2 * n - 1

for i in range(n):
    stars = ' '.join(['*'] * (i + 1))
    space_num = (max_len - len(stars)) // 2
    print(' ' * space_num + stars)
