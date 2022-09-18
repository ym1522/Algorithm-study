import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def solution(nums, N):
    i = 0
    while i < 2 * N - 3:
        j, p = i + 1, i + 2
        while nums[i] != nums[p] and p < 2 * N - 1:
            p += 1
        
        while j < p:
            for q in range(p + 1, 2 * N):
                if nums[j] == nums[q]:
                    return False
            j += 1
        i += 1
    return True

print("YES") if solution(nums, N) else print("NO")