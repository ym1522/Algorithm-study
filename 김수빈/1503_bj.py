import sys

def solution(N, nums):
    minimum = None
    left_nums = list(filter(lambda x: not x in nums, range(1, 1000 + 2)))
    for i in range(len(left_nums)):
        k, j = 0, len(left_nums) - 1
        while k <= j:
            val = left_nums[i] * left_nums[k] * left_nums[j]
            minimum = abs(N - val) if minimum is None or abs(N - val) < minimum else minimum
            if val > N:
                j -= 1
            elif val < N:
                k += 1
            else:
                minimum = 0
                break

    return minimum

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

print(solution(N, nums))