n = int(input())

def recursive(n):
    if n == 1:
        return
    
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            return recursive(n // i)
        
recursive(n)