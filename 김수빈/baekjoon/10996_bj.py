n = int(input())

first_row = ' '.join(['*'] * (n - n // 2))
second_row = ' ' + ' '.join(['*'] * (n // 2))

second_row = second_row if n > 1 else ''

for i in range(n):
    print(first_row)
    print(second_row)