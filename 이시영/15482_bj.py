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

'''
# 시간초과가 남.. 최대 1000글자로 이루어져서 재귀로 돌리기엔 많은듯? dp로 바꿈
from sys import stdin
import sys
sys.setrecursionlimit(10**6)
def LCS(a,b):
    if len(a)==0 or len(b)==0:
        return 0
    else:
        if a[-1]==b[-1]:
            return LCS(a[:len(a)-1], b[:len(b)-1])+1
        else:
            return max(LCS(a,b[:len(b)-1]), LCS(a[:len(a)-1],b))
            
                
a = stdin.readline().rstrip()
b = stdin.readline().rstrip()

print(LCS(a,b))
'''