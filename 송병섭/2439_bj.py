a = int(input())
count = 1
while True:
    if count== a+1:
        break
    else:
        print(('*' * count).rjust(a))
        count +=1