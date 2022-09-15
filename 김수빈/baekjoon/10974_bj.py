import sys
from itertools import permutations

N = int(sys.stdin.readline())
nums = list(range(1, N + 1))
cases = list(permutations(nums, N))
answer = ""
for c in cases:
    answer += ' '.join(list(map(str, c))) + "\n"
print(answer)