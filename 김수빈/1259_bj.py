import sys

nums = list(map(lambda x: x.strip(), sys.stdin.readlines()))[:-1]
for n in nums:
    if n == n[::-1]: print("yes")
    else: print("no")