while True:
    first, second = map(int,input().split())
    if first == 0 & second == 0:
        break
    elif first > second:
        print("Yes")
    else:
        print("No")