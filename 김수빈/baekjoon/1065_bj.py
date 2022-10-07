import sys

N = int(sys.stdin.readline())
cnt = 0

# N부터 1까지 완전 탐색
for i in range(N, 0, -1):    
    if len(str(i)) == 1:
        cnt += 1
        continue
    nums = list(map(int, str(i)))
    diff = [0] * (len(nums) - 1)
    for i in range(len(nums) - 1):
        diff[i] = nums[i + 1] - nums[i]
    if len(set(diff)) == 1:
        cnt += 1
print(cnt)