n = int(input())
max_len = 2 * n - 1

for i in range(n - 1):
    stars = '*' + ' ' * (2 * i - 1) + '*' if i > 0 else '*' 
    space_num = (max_len - len(stars)) // 2
    print(' ' * space_num + stars)

print('*' * max_len)


