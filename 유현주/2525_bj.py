h, m = map(int,input().split())
t = int(input())

hour = (h*60 + m + t)//60

if m+t >= 60:
    if hour >= 24:
        print(hour-24,(h*60 + m + t)%60)
    else:
        print(hour,(h*60 + m + t)%60)

else:  
    print(h, m+t)