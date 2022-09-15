import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readlines()))
nums = nums[::-1]

stack = []
for n in nums:
    if not stack or stack[-1] > n:
        stack += [n]
print(len(stack))