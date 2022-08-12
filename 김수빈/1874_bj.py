import sys

def solution(nums):
    stack = []
    answer = []

    cur_n = 1
    seq = []
    for i in range(len(nums)):
        while cur_n <= nums[i]:
            stack += [cur_n]
            answer += ["+"]
            cur_n += 1 

        while stack and stack[-1] >= nums[i]:
            seq += [stack.pop()]
            answer += ["-"]
    
    if nums != seq:
        return ["NO"]
    return answer

nums = list(map(int, sys.stdin.readlines()))[1:]
answer = solution(nums)
print('\n'.join(answer))