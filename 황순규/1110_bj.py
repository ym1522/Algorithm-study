n = int(input())
num=n
cnt=1
while True:
    num= (num%10)*10 + (num//10 + num%10)%10
    if num == n:
        print(cnt)
        break
    cnt+=1