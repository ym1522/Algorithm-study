import sys

def search_binary(lines, min_len, max_len):
    if min_len == max_len:
        cnt = sum(list(map(lambda x: x // min_len, lines)))
        return min_len if cnt >= N else -1
        
    mid = (min_len + max_len) // 2
    cnt = sum(list(map(lambda x: x // mid, lines)))
    
    if cnt >= N:
        right = search_binary(lines, mid + 1, max_len)
        return right if right > 0 else mid
    else:
        return search_binary(lines, min_len, mid)

K, N = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readlines()))
sum_lines = sum(lines)

min_length = max(list(map(lambda x: x // N, lines)))
print(search_binary(lines, max(min_length, 1), sum_lines // N))