import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    stars = ''
    temp = ''
    
    for j in range(int(((2 * N - 1) - (2 * i - 1)) / 2)):
        temp = temp + ' '

    for k in range(2 * i - 1):
        stars = stars + '*'

    print(temp + stars)