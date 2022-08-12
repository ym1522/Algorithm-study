import sys
n = int(sys.stdin.readline())
data = [0] * 10001
for i in range(n):
    data[int(sys.stdin.readline())] += 1
for i in range(10001):
    if data[i] != 0:
        for j in range(data):
            print(i)

# ---------- 메모리 초과 ㅠㅠ ..-------#
#for i in range(n):
#    data.append((int(sys.stdin.readline())))
#data.sort(reverse = False)

#for i in data:
#    print(i)
# ------------------------------------#