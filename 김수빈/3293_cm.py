import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

stack = []
stt, end = -1, -2
for i, n in enumerate(nums):
    if not stack or stack[-1][-1] <= n:
        stack += [(i, n)]
        continue
    j = len(stack) - 1
    while n < stack[j][-1] and j >= 0:
        j -= 1
    stt = max(0, stack[j][0] + 1) if stt < 0 or max(0, stack[j][0] + 1) < stt else stt
    end = i
print(end - stt + 1)