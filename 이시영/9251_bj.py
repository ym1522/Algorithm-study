# 15482와 같음. 15482는 한글 LCS인데 파이썬은 영어, 한글 상관없이 할 수 있어서
from sys import stdin

def LCS(a,b):
    dp=[0]*1000
    for i in range(len(a)):
        max_dp = 0
        for j in range(len(b)):
            if max_dp<dp[j]:
                max_dp=dp[j]
            elif a[i]==b[j]:
                dp[j]=max_dp+1
    return max(dp)

a = stdin.readline().rstrip()
b = stdin.readline().rstrip()

print(LCS(a,b))