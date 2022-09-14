import sys


N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

def binary_search(target):
    N_list.sort()
    start = 0
    end = len(N_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if N_list[mid] == target:
            return 1
        elif N_list[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return 0


for i in M_list:
    print(binary_search(i), end = ' ')