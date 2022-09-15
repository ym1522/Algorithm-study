import sys

N = int(sys.stdin.readline())
string = list(sys.stdin.readline().strip())

r, M = 31, 1234567891
answer = 0
R = 1
for s in string:
    answer += ((ord(s) - 96) * R)
    R *= r
print(answer % M)