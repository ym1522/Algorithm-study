import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readlines()))
nums.sort()

print(round(sum(nums) / N))
print(nums[N // 2])

D = {}
for n in nums:
    if not n in D: D[n] = 1
    else: D[n] += 1
D_sorted = sorted(D.items(), key=lambda x: x[-1], reverse=True)
D_sorted = list(filter(lambda x: x[1] == D_sorted[0][1], D_sorted))
D_sorted = sorted(D_sorted, key=lambda x: x[0])

print(D_sorted[0][0]) if len(D_sorted) == 1 else print(D_sorted[1][0])

print(nums[-1] - nums[0])