import sys
sys.setrecursionlimit(10 ** 9)

# 피보나치 수 3과 동일한 방식으로 접근
LIMIT = 1000000007
D = {}
def fibo(N):
    if N <= 2: return 1 if N > 0 else 0
    if N in D: return D[N]

    if N % 2 == 0:
        n = N // 2
        n_1 = n - 1
    else:
        n = (N + 1) // 2
        n_1 = N - n
    
    fn = D[n] if n in D else fibo(n)
    fn_1 = D[n_1] if n_1 in D else fibo(n_1)
    answer = ((2 * fn_1 + fn) * fn) % LIMIT if N % 2 == 0 else (fn ** 2 + fn_1 ** 2) % LIMIT
    
    D[n] = fn
    D[n_1] = fn_1
    D[N] = answer
    return answer

N = int(sys.stdin.readline())
print(fibo(N))