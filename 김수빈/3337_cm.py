import sys

def solution(N, A):
    for i in range(N):
        j = N - 1
        while j > i:
            k = j - 1
            m = i + 1
            while m < k:
                mul_1 = A[i] * A[j]
                mul_2 = A[m] * A[k]
                if mul_1 == mul_2: return "YES"
                elif mul_2 > mul_1:
                    k -= 1
                else:
                    m += 1
            j -= 1
    return "NO"

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

print(solution(N, A))