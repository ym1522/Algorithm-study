import sys
N = int(sys.stdin.readline())
i = 0
slot_num = 1
while slot_num < N:
    slot_num += i + 1
    i += 1
print(i)