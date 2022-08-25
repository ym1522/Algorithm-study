n = input()
arr = [0 for _ in range(10)]

for i in n:
    if int(i) == 9:
        arr[6] += 1
    else:
        arr[int(i)] += 1
arr[6] = (arr[6]+1) // 2
print(max(arr))