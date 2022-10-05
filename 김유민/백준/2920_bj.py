import sys

arr = list(map(int, sys.stdin.readline().split(' ')))
print('ascending' if arr == [1, 2, 3, 4, 5, 6, 7, 8] else 'descending' if arr == [8, 7, 6, 5, 4, 3, 2, 1] else 'mixed')