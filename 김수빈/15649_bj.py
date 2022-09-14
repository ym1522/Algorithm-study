import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
nums = list(range(1, N + 1))
cases = list(permutations(nums, M))
answer = ""
for c in cases:
    answer += ' '.join(list(map(str, c))) + "\n"
print(answer)