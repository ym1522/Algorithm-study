import sys

n = int(sys.stdin.readline())
str = sys.stdin.readline().rstrip()
res = 0

for i, s in enumerate (str):
    res += ((ord(s)-96) * 31**i)

print(res% 1234567891)  # mod 연산 해 줘야 100점