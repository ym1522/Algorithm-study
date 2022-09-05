import sys
K = int(sys.stdin.readline())
fermat = [3, 5, 17, 257, 65537]
while K % 2 == 0:
    K //= 2
for d in fermat:
    if K % d == 0: K //= d       
print("YES") if K == 1 else print("NO")