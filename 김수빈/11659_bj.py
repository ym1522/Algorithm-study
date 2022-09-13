import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
inputs = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))

acc_sums = [0] * N
acc_sums[0] = nums[0]
for i in range(1, N):
    acc_sums[i] = acc_sums[i - 1] + nums[i]    

for i, j in inputs:
    prev_acc = acc_sums[i - 2] if i > 1 else 0
    print(acc_sums[j - 1] - prev_acc)