import copy

def solution(nums, N):
    prev_scores = [1] * (N + 1)
    cur_scores = [1] * (N + 1)

    for i in range(1, N + 1):        
        for j in range(i + 1, N + 1):
            if nums[j - 1] > nums[i - 1]:
                cur_scores[j] = max(prev_scores[j], prev_scores[i] + 1)
            else:
                cur_scores[j] = prev_scores[j]

        prev_scores = copy.deepcopy(cur_scores)
    return max(cur_scores)

N = int(input())
nums = list(map(int, input().split()))

print(solution(nums, N))