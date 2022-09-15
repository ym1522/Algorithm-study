import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readlines()))

nums.sort()
for n in nums:
    print(n)