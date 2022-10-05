from sys import stdin

def fin(n):
    if n==0:
        return 0
    if dp[n]==0:
        dp[n]=fin(n-1)+fin(n-2)
    return dp[n]

n = int(stdin.readline())
dp = [0]*46
dp[0]=0
dp[1]=1
print(fin(n))