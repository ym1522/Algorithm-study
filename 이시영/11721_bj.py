from sys import stdin

n = stdin.readline().rstrip()

for i in range(0,len(n),10):
    print(n[i:i+10])