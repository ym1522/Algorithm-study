import sys

def solution(nums, N):    
    values = [[0] * N for _ in range(N)]
    values[0][0] = nums[0][0]
    for i in range(1, N):
        for j in range(i + 1):
            values[i][j] = max([values[i][j],
                                values[i - 1][j] + nums[i][j], 
                                values[i - 1][j - 1] + nums[i][j]])
    return max(values[-1])

N = int(sys.stdin.readline())
nums = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
print(solution(nums, N))