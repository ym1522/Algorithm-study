from functools import reduce
n = int(input())

print(reduce(lambda x, y: x + y, range(1, n + 1)))