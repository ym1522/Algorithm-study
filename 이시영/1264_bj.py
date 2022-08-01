while True:
    arr=input()
    count=0
    if arr=='#':
        break
    for i in arr:
        if i in 'aeiouAEIOU':
            count+=1
    print(count)