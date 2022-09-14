def binary_search(target, start, end, data):
    while start<=end:
        mid=(start+end)//2
        if data[mid]==target:
            return mid
        elif data[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return -1

from sys import stdin

n=int(stdin.readline())
str1=list(map(int, stdin.readline().split()))
m=int(stdin.readline())
str2=list(map(int, stdin.readline().split()))

str1.sort()

for i in range(m):
    if binary_search(str2[i], 0, n-1, str1) != -1:
        print("1", end=" ")
    else:
        print("0", end=" ")