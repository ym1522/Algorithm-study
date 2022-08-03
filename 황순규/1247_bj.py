import sys

for i in range(3):    
    N = int(sys.stdin.readline())
    sum = 0
    for i in range(N):
        sum += int(sys.stdin.readline())
        
    if sum > 0:
        print("+")
    elif sum < 0:
        print("-")
    else:
        print("0")