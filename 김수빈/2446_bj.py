n = int(input())
max_star = 2 * n - 1

indices = list(range(n - 1, 0, -1))+ list(range(n)) 
for i in indices:
    star_num = 2 * i + 1
    space_num = (max_star - star_num) // 2
    print(' ' * space_num + '*' * star_num)
