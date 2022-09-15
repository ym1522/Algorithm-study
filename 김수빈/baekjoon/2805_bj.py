import sys

def search_binary(heights, M, min_h, max_h):
    if min_h == max_h:
        total_tree = sum(list(map(lambda x: max(x - min_h, 0), heights)))
        return min_h if total_tree >= M else -1
        
    mid = (min_h + max_h) // 2
    total_tree = sum(list(map(lambda x: max(x - mid, 0), heights)))
    if total_tree > M:
        right = search_binary(heights, M, mid + 1, max_h)
        return right if right > 0 else mid
    
    elif total_tree == M:
        return mid
    else:
        return search_binary(heights, M, min_h, mid)

N, M = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

print(search_binary(heights, M, min_h=0, max_h=max(heights)))