data = ["a","e","i","o","u"]
while True:
    count = 0
    S = input().lower()
    if S == "#":
        break
    for i in(S):
        if i in data:
            count += 1
    print(count)  