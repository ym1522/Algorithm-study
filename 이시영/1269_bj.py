# 대칭 차집합은 합집합-교집합으로도 구할 수 있음
from sys import stdin

n, m = map(int,stdin.readline().split())

a = set(map(int, stdin.readline().split()))
b = set(map(int, stdin.readline().split()))

print(len(a|b)-len(a&b))