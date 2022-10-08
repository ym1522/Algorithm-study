from sys import stdin

ch=[i**2 for i in map(int,stdin.readline().split())]
print(sum(ch)%10)