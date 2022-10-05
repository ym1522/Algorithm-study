import sys
sys.setrecursionlimit(10 ** 9)

# 피보나치 수열
LIMIT = 1000000007
def fibo(N):
    if N < 2: return N
    elif N == 2: return 1
    mid = N // 2
    if N % 2 == 0:
        fn = fibo(mid)
        return ((2 * fibo(mid - 1) + fn) * fn) % LIMIT
    else:
        return (fibo(mid) ** 2 + fibo(N - mid) ** 2) % LIMIT

N = int(sys.stdin.readline())    
print(fibo(N))