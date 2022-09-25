# set는 교집합을 사용할 수 있어서 set 이용함
from sys import stdin

n, m = map(int,stdin.readline().split())

noear = set(stdin.readline().strip() for _ in range(n))
nosee = set(stdin.readline().strip() for _ in range(m))

earsee=sorted((noear & nosee))
print(len(earsee))
print('\n'.join(earsee))