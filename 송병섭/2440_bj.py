a = int(input())
count = a
while True:
    if count == 0:
        break
    else:
        print('*' * count)
        count -= 1