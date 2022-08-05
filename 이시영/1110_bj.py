N = int(input())
NN = N
count = 0
while(True):
    a = NN//10
    b = NN%10
    c = (a+b)%10
    NN = b*10 + c
    count+=1
    if N == NN:
        break

print(count)