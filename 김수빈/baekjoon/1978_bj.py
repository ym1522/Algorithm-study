import sys

def is_prime(nums):
    if not nums: return 0
    max_val = max(nums)
    cands = [0] * (max_val + 1)
    for n in nums:
        cands[n] = 1 if n > 1 else 0
        
    for i in range(2, max_val + 1):
        for j in range(i + 1, max_val + 1):
            if j % i == 0:
                cands[j] = 0
                
    return cands.count(1)

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(is_prime(nums))