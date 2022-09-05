import sys

n = sys.stdin.readline()
count = 0

for i in range(len(n)):
    if n[i] == str(3) or n[i] == str(6) or n[i] == str(9):
        count += 1

if count == 0: print(n, end='')
else: print('clap'*count)