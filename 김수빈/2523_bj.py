n = int(input())

indices = list(range(1, n)) + list(range(n, 0, -1))
for i in indices:
    print('*' * i)