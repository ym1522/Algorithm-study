import sys

a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
b.sort(reverse = True)
first = 0
second = 0 
for i in b:
    if b.count(i) >= 2:
        if first == 0:
            first = i
            b.remove(i)
            b.remove(i)
            break
        elif second == 0:
            second = i
            
for i in b:
    if b.count(i) >= 2:
        if first == 0:
            first = i
            b.remove(i)
            b.remove(i)
        elif second == 0:
            second = i
            b.remove(i)
            b.remove(i)
            break
result = first * second
    

print(result)
