import sys

def get_factor(n):
    if n == 1:return []
    
    for i in range(2, n + 1):
        if n % i == 0:
            return [i] + get_factor(n // i)

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

answer = [1]
factors = get_factor(nums[0])
for i in factors:
    if (N == 2 and nums[1] % i == 0) or (N == 3 and nums[1] % i == 0 and nums[2] % i == 0):
        nums = list(map(lambda x: x // i, nums))
        answer += list(map(lambda x: x * i, answer))

answer = list(set(answer))
answer.sort()
for i in answer:
    print(i)