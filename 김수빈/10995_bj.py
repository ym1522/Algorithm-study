n = int(input())

for i in range(1, n + 1):
    row = ' ' if i % 2 == 0 else ''
    row += ' '.join(['*'] * n)
    print(row)