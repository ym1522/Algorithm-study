import sys

S = int(sys.stdin.readline())
acc_sum = 1
i = 1
while acc_sum + i + 1 <= S:
    acc_sum += i + 1
    i += 1
    
print(i)