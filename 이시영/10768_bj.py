months=int(input())
day=int(input())

if months==2 and day==18:
    print("Special")
elif months > 2 or (months==2 and day>18):
    print("After")
else:
    print("Before")