from sys import stdin

box = list(map(int,input().split()))
che=[1,1,2,2,2,8]
for i in range(len(box)):
    print(che[i]-box[i], end=" ")