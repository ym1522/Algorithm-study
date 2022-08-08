import sys

numbers = list(map(int,sys.stdin.readlines())) #3 0 0 0 10 1 2 4 8 16 32 64 128 256 -512
result = 0
i = 0
while True:
    for j in range (i+1, numbers[i]+i+1):
        result += numbers[j] 
    if result  == 0:
        print('0')
    elif result < 0:
        print('-')
    else : print('+')
    i += numbers[i] + 1
    result = 0
    if i >= len(numbers): break