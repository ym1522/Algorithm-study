import sys

N = int(sys.stdin.readline())

temps = {i:0 for i in range(1, 31)}

for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    
    for i in range(s, e+1):
        temps[i] += 1

print(max(temps, key = temps.get))