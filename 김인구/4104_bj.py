while True:
    n, m = map(int, input().split())
    
    if n==0 and m==0:
        break
    else:
        print("Yes") if n > m else print("No")