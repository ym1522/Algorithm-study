import sys

def Felindrom(s1, s2):
    temp = s1 + s2
    flag = True
    for i in range(len(temp) // 2):
        if temp[i] != temp[-i-1]:
            flag = False
            break
    return flag

def find(k):
    words = [sys.stdin.readline().strip() for _ in range(k)]
    for i in range(k-1):
        for j in range(i+1, k):
            if Felindrom(words[i], words[j]):
                return words[i] + words[j]
            if Felindrom(words[j], words[i]):
                return words[j] + words[i]
    return 0
            
    
    
T = int(sys.stdin.readline())
for i in range(T):
    k = int(sys.stdin.readline())
    print(find(k))
    
        