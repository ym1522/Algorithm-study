flags = [False] + [True] * 10000

def seq(n):
    n = str(n)
    temp = 0
    for i in n:
        temp += int(i)
    temp += int(n)
    
    return temp
    

for i in range(1, 10001):
    temp = i
    while True:
        temp = seq(temp)
        if temp > 10000:
            break
        else:
            flags[temp] = False
            
for i in range(len(flags)):
    if flags[i]:
        print(i)