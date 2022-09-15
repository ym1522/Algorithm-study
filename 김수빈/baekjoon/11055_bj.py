import copy

def solution(nums, N):
    sums = copy.copy(nums)

    for i in range(N):
        prev_sums = copy.copy(sums)
        for j in range(i-1, -1, -1):
            if nums[i] > nums[j]:
                sums[i] = max(sums[i], prev_sums[j] + prev_sums[i])
    
    return max(sums)


N = int(input())
nums = list(map(int, input().split()))

print(solution(nums, N))