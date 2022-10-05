def fibonacci_iter(n):
    if n == 0: return (1, 0)
    if n == 1: return (0, 1)
    
    arr = [(1, 0), (0, 1)] 

    for i in range(2, n):
        arr += [(arr[i-1][0] + arr[i-2][0], arr[i-1][1] + arr[i-2][1])]
    
    return (arr[-1][0] + arr[-2][0], arr[-1][1] + arr[-2][1])

cnt = int(input())

for i in range(cnt):
    X = int(input())
    zero, one = fibonacci_iter(X)
    print(f"{zero} {one}")