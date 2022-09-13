import sys

nums = []

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    else:
        nums.append(list(map(int, str(N))))

for i in nums:
    if i == list(reversed(i)):
        print('yes')

    else:
        print('no')