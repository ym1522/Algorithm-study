n=input()
m=[]
n=n.upper()
cnt=list(set(n))

for i in cnt:
    count = n.count(i)
    m.append(count)
    
if m.count(max(m))>1:
    print("?")
else:
    print(cnt[m.index(max(m))])