import sys

S = int(sys.stdin.readline())

num = 1
temp = 1

while num + temp < S:
    num += temp + 1
    temp += 1
print(temp)