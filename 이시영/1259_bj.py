while True:
    n = input()
    if n=='0': break
    if n == n[::-1]:  # 문자열 뒤집기
        print("yes")
    else:
        print("no")