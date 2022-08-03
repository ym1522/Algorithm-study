import sys

for i in range(3):    
    N = int(sys.stdin.readline()) # 시간 초과 발생할 때 input() 대신 사용
    sum = 0
    for i in range(N):
        sum += int(sys.stdin.readline())
        
    if sum > 0:
        print("+")
    elif sum < 0:
        print("-")
    else:
        print("0")