import sys

n = int(sys.stdin.readline())

arr = []
count = 1

for i in range(n):
    s = int(sys.stdin.readline())
    arr.append(s)

top = arr.pop()

for i in range(n - 1):
    tmp = arr.pop()
    if top < tmp:
        top = tmp
        count += 1

print(count)