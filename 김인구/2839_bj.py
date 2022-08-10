n = int(input())

cnt = 0 

while True:
    
    # 5의 배수 or 0
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    
    # not % 5
    n -= 3
    cnt += 1
    
    if n < 0:
        print(-1)
        break