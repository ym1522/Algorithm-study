N = int(input())

for i in range(2, N+1):
    if N == 1:
        break
    
    while True:
        if N % i == 0:
            print(i)
            N /= i
        else:
            break