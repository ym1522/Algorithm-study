import sys

N = sys.stdin.readline()
num_list = list(N)
num_clap = ["3", "6", "9"]
cnt = 0

for i in num_clap:
    cnt += num_list.count(i)

if cnt == 0:
    print(int(N))
else:
    print('clap' * cnt)