import sys
N, K = map(int, sys.stdin.readline().split())

def solution(N, K):
    if K > N or K < 0: return 0
    
    n_factorial, k_factorial, n_k_factorial = 1, 1, 1
    
    for i in range(1, N + 1):
        n_factorial *= i
        if i <= K:
            k_factorial *= i
        if i <= N - K:
            n_k_factorial *= i
    return int(n_factorial / (k_factorial * n_k_factorial))
print(solution(N, K))