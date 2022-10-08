from sys import stdin

def divide(N, R, C):
    global cnt
    if r == R and c == C:
        print(int(cnt))
        exit(0)
    if not (R <= r < R + N and C <= c < C + N):
        cnt += N * N
        return
    divide(N/2, R, C) # 1사분면
    divide(N/2, R, C + N/2) # 2사분면
    divide(N/2, R + N/2, C) # 3사분면
    divide(N/2, R + N/2, C + N/2) # 4사분면

n,r,c=map(int,stdin.readline().split())
cnt=0

divide(2**n, 0, 0)