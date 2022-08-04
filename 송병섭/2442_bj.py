a = int(input())
count = 0
while True:
    if count== a:
        break
    else:
        print(' '*(a - count - 1) + '*' * (2 * count+1))
        count +=1