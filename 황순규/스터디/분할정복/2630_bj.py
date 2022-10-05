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
        if p[0] == 0:
            w_cnt += 1
        else:
            b_cnt += 1
    
    else:
        flag0 = -1
        flag1 = -1
        
        for i in range(len(p)):

            if p[i].count(0) == len(p):
                flag0 = 0
            else:
                flag0 = -1
                break
                
        for i in range(len(p)):
            if p[i].count(1) == len(p):
                flag1 = 1
            else:
                flag1 = -1
                break
 
        if flag0 == -1 and flag1 == -1:
            arr1, arr2, arr3, arr4 = slice(p)
            return divide(arr1), divide(arr2), divide(arr3), divide(arr4)
        elif flag0 == 0:
            w_cnt += 1
        elif flag1 ==1:
            b_cnt += 1
            
            
            
divide(paper)

print(b_cnt)
print(w_cnt)