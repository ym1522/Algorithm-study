N = int(input())
n = N

for i in range(N):
    for j in range(1, n + 1):
        print("*", end = "")
        
    n -= 1
        
    print()