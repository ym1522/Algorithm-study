from sys import stdin

t = int(stdin.readline())

for i in range(t):
    arr=[]
    k = int(stdin.readline())
    
    for i in range(k):
        arr.append(stdin.readline().rstrip())
        
    con = []
    for i in range(k):
        for j in range(i+1,k):
            con.append(arr[i]+arr[j])
            con.append(arr[j]+arr[i])
    
    check=0
    for i in con:
        if i == i[::-1]:
            check=i
    print(check)