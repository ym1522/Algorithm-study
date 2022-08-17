import sys

N = int(sys.stdin.readline())
N_lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_lst = list(map(int, sys.stdin.readline().split()))
N_lst.sort()


l = 0
r = len(N_lst) -1
for i in M_lst:
    while l <= r:
        mid = (l+r) // 2
        
        if N_lst[mid] == i:
            print('1', end=' ')
                    
        elif N_lst[mid] > i:
            r = mid -1
        
        else:
            l = mid +1
    print('0',end=' ')