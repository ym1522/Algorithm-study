n = int(input())
data = list(map(int, input().split()))
x = int(input())

data.sort()
left = 0
right = n-1
cnt = 0
while left < right:
    ans = data[left] + data[right]
    
    if ans == x:
        cnt += 1
    if ans < x:
        left += 1
    else:
        right -= 1
        
print(cnt)
