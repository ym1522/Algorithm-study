import sys

def solution(N):
    nums = list(range(1, N + 1))
    del_last = False
    while len(nums) > 1:
        if not del_last:
            indices = list(filter(lambda x: x % 2 > 0, range(len(nums))))
        else:
            indices = list(filter(lambda x: x % 2 == 0, range(len(nums))))
        last = nums[-1]
        nums = list(map(lambda x: nums[x], indices))
        del_last = not last in nums
    return nums[0]

N = int(sys.stdin.readline())
print(solution(N))