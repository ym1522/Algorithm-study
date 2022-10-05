data = input()

n = ['ABC', 'DEF','GHI', 'JKL', 'MNO','PQRS', 'TUV', 'WXYZ']

cnt = 0

for i in data:
    for j in n:
        if i in j:
            cnt += n.index(j) +3
            
print(cnt)