while(True):
    a = input()
    if a == "0":
        break
    # 사실 인덱싱 사용하면 편리하다는 것을 알았기에..
    elif a == a[::-1]:
        print("yes")
    else:
        print("no")