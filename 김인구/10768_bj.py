m = int(input())
d = int(input())

# case1
if m < 2 :
    print("Before")

# case2
elif m == 2:
    if d < 18:
        print("Before")
    elif d == 18:
        print("Special")
    else:
        print("After")

# case3
else:
    print("After")