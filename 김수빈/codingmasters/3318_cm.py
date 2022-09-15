import sys

def get_divisor(n):
    answer = [1]
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            answer += [i, n // i]
    
    return answer

A, B = map(int, sys.stdin.readline().split())
A_divisor = get_divisor(A)
B_divisor = get_divisor(B)

if sum(A_divisor) == B and sum(B_divisor) == A:
    print("YES")
else:
    print("NO")