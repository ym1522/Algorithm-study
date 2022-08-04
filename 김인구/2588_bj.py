a = int(input())
b = int(input())

ans = 0
cnt = 0
result = 0
while b>0:
    c = b%10
    b = b//10 
    
    ans = a*c
    
    result += ans*((10)**cnt)
    cnt += 1

    print(ans)
print(result)
    