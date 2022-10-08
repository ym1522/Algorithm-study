import sys

N = int(sys.stdin.readline())

paper = []
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))


def slice(arr):
    arr1, arr2, arr3, arr4 = [], [], [], []
    for i in arr[:len(arr)//2]:
        arr1.append(i[:len(arr)//2])
        arr2.append(i[len(arr)//2:])
    for i in arr[len(arr)//2:]:
        arr3.append(i[:len(arr)//2])
        arr4.append(i[len(arr)//2:])
        
    return arr1, arr2, arr3, arr4

global w_cnt, b_cnt
w_cnt, b_cnt = 0, 0

def divide(p):
    global w_cnt, b_cnt
         
    if len(p) == 1:
        if p[0][0] == 0:
            w_cnt += 1
            return
        else:
            b_cnt += 1
            return
    
    else:        
        s = []
        for i in p:
            s += list(set(i))
        s = list(set(s))
        
        if len(s) > 1:
            arr1, arr2, arr3, arr4 = slice(p)
            return divide(arr1), divide(arr2), divide(arr3), divide(arr4)
        elif s[0] == 0:
            w_cnt += 1
            return
        elif s[0] ==1:
            b_cnt += 1
            return
divide(paper)

print(w_cnt) 
print(b_cnt)