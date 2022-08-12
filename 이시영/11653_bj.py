n=int(input())

i=2
while True:
    if n==1:
        break
    if n%i==0:
        n=n/i
        print(i)
    else:
        i+=1