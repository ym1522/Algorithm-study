import sys

N, B = map(int, sys.stdin.readline().split())

# 나머지가 10보다 큰 경우 알파벳 사용
D = [chr(i) for i in range(65, 91)]

# N을 B진법으로 표기하는 문제
answer = ""
while N >= B:
    remain = N % B
    N //= B 
    if remain < 10:
        answer = str(remain) + answer
    else:
        answer = D[remain-10] + answer
if N < 10:
    answer = str(N) + answer
elif N > 0:
    answer = D[N - 10] + answer
print(answer)