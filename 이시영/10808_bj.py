s=input()
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count=[0]*26
for i in s:
    for j in range(len(alpha)):
        if i==alpha[j]:
            count[j]+=1

for i in count:
    print(i, end=' ')